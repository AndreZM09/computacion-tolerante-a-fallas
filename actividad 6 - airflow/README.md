
# Mi Primer DAG en Apache Airflow

Este repositorio contiene un ejemplo básico de un Directed Acyclic Graph (DAG) creado para ser utilizado con Apache Airflow.

### Descripción del Código

- **Importación de Módulos:** Se importan los módulos necesarios de Airflow y Python para construir el DAG.

- **Función `print_hello()`:** Esta función define una tarea Python que simplemente devuelve el string 'Hola, Airflow!'.

- **`default_args`:** Este diccionario contiene argumentos predeterminados que se aplicarán a todas las tareas del DAG.

- **Definición del DAG:** La instancia `dag` es creada usando el constructor `DAG()`, y configura las propiedades del DAG, como la programación y los argumentos predeterminados.

- **Tareas:** `start_task`, `hello_task`, y `end_task` son tareas definidas dentro del DAG, utilizando operadores de Airflow para especificar la lógica de las tareas.

- **Dependencias de Tareas:** La última línea especifica el orden en que las tareas deben ejecutarse utilizando el operador "bitshift" (`>>`) para establecer las dependencias entre las tareas.

## Cómo Ejecutar el DAG

1. **Instalar Apache Airflow:** Asegúrate de tener Apache Airflow instalado y configurado en tu entorno local o en un contenedor Docker.

2. **Ubicar el DAG:** Coloca el archivo del código DAG en la carpeta `dags` de tu instalación de Airflow.

3. **Iniciar Airflow:** Inicia el web server y el scheduler de Airflow con los siguientes comandos:
   ```bash
   airflow webserver
   ```
   ```bash
   airflow scheduler
   ```
   
4. **Interfaz Web de Airflow:** Abre la interfaz web de Airflow en tu navegador, normalmente accesible en `http://localhost:8080`, y deberías ver tu DAG `mi_primer_dag` listado en la interfaz.

5. **Ejecutar el DAG:** Para ejecutar el DAG, puedes activarlo en la interfaz web y debería comenzar a ejecutarse en el próximo intervalo de programación.
