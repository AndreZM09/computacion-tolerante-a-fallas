# Flujo ETL con Prefect

## Descripción General
Este repositorio contiene un flujo básico ETL (Extraer, Transformar, Cargar) utilizando Prefect para extraer datos desde una API REST, transformar esos datos en un formato utilizable y finalmente cargarlos en una base de datos SQLite.

## Estructura del Proyecto
- **get_task_data**: Extrae datos de la API.
- **parse_task_data**: Transforma los datos brutos en un formato utilizable.
- **store_tasks**: Carga los datos transformados en una base de datos SQLite.

## Requisitos
- Python 3.7+
- Prefect
- Requests
- SQLite

## Instalación
Instala las dependencias utilizando pip:

```bash
pip install prefect requests
```

## Uso
1. Configuración de la Base de Datos
Asegúrate de tener SQLite instalado y configurado en tu máquina.

2. Ejecución del Flujo
Simplemente ejecuta el script en Python para iniciar el flujo ETL:

python etl_flow.py

## Descripción de las Tareas
1. get_task_data
Realiza una solicitud GET a un endpoint y retorna la respuesta en JSON. Asegúrate de tener acceso al endpoint y que este esté operativo.

2. parse_task_data
Convierte los datos brutos (en este caso, JSON) en un formato que pueda ser cargado en la base de datos. Asegúrate de que los campos que estás intentando descomprimir coincidan con la respuesta de la API.

3. store_tasks
Carga los datos en una base de datos SQLite. Asegúrate de que la estructura de la tabla en la base de datos coincida con los datos que estás intentando insertar.


