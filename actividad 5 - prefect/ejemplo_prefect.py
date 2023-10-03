from prefect import task, Flow
from collections import namedtuple
from contextlib import closing
import json
import requests
import sqlite3

@task
def get_task_data():
    try:
        r = requests.get("https://jsonplaceholder.cypress.io/todos/1")
        r.raise_for_status()  # Raise an error for bad responses
        return r.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except json.JSONDecodeError:
        print("Failed to decode JSON response")

@task
def parse_task_data(raw):
    if raw is None:
        return []
    
    Task = namedtuple('Task', ['userId', 'id', 'title', 'completed'])
    try:
        return [Task(**raw)]
    except TypeError as e:
        print(f"Failed to parse task data: {e}")
        return []

@task
def store_tasks(parsed):
    create_cmd = """
    CREATE TABLE IF NOT EXISTS tasks (
        userId INTEGER,
        id INTEGER,
        title TEXT,
        completed BOOLEAN
    )
    """
    insert_cmd = "INSERT INTO tasks VALUES (?,?,?,?)"
    
    with closing(sqlite3.connect("tasks.db")) as conn:
        with closing(conn.cursor()) as cursor:
            try:
                cursor.execute(create_cmd)
                cursor.executemany(insert_cmd, parsed)
                conn.commit()
            except sqlite3.Error as e:
                print(f"Database error: {e}")

with Flow(name="task etl flow") as task_etl_flow:
    raw = get_task_data()
    parsed = parse_task_data(raw)
    store_tasks(parsed)

# Run the flow
task_etl_flow.run()
