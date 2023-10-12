from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hola, Airflow!'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'mi_primer_dag',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
)

start_task = DummyOperator(
    task_id='Inicio',
    dag=dag,
)

hello_task = PythonOperator(
    task_id='Hola',
    python_callable=print_hello,
    dag=dag,
)

end_task = DummyOperator(
    task_id='Fin',
    dag=dag,
)

start_task >> hello_task >> end_task
