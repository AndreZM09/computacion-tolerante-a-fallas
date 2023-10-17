# Tienda de Deportes XYZ 🏀🚴‍♂️🎾

Este proyecto es una tienda de deportes en línea construida con Node.js y Express, y utiliza Bootstrap para el front-end. La aplicación ha sido contenida usando Docker para asegurar un despliegue uniforme y fácil.

## 📋 Prerrequisitos

- **Docker**: Debes tener Docker instalado en tu máquina. Si aún no lo tienes, puedes descargarlo y obtener instrucciones de instalación desde [Docker oficial](https://www.docker.com/get-started).

## 🚀 Instrucciones para ejecutar el proyecto con Docker

1. **Construir la imagen Docker**:

   Una vez estés en la raíz del proyecto, construye la imagen Docker usando el siguiente comando:

   ```bash
   docker build -t tienda-deportes:latest .
   ´´´

2. **Ejecutar el contenedor**:

   Luego de construir la imagen, puedes ejecutar el contenedor usando:

   ```bash
   docker run -p 3000:3000 tienda-deportes:latest
   ´´´
    Esto mapeará el puerto 3000 de tu máquina local al puerto 3000 del contenedor, lo que significa que podrás acceder a la aplicación en tu navegador web en http://localhost:3000.

3. **Verificar**:

   Abre tu navegador y dirígete a http://localhost:3000 para ver la aplicación en acción.