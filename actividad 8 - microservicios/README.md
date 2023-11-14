# Microservicios de Autenticación y Perfil de Usuario

Esta es una aplicación simple que demuestra el uso de microservicios para autenticación y gestión de perfiles de usuario.

## Requisitos

- Python (versión 3.6 o superior)
- Flask (instalado a través de `pip install Flask`)

## Ejecución de los Microservicios

1. Abre una terminal y navega al directorio donde se encuentra el archivo `auth_service.py`.
2. Ejecuta el siguiente comando para iniciar el microservicio de autenticación:
   ```bash
   python auth_service.py
   ```
3. Abre otra terminal y navega al directorio donde se encuentra el archivo `user_service.py`.
4. Ejecuta el siguiente comando para iniciar el microservicio de perfil de usuario:
   ```bash
   python user_service.py
   ```
Ambos servicios se ejecutarán en los puertos 5001 y 5002 respectivamente

## Pruebas de los Microservicios
- Para autenticar, abre un navegador y accede a http://127.0.0.1:5001/authenticate/usuario/contrasena.

- Para obtener el perfil del usuario autenticado, abre un navegador y accede a http://127.0.0.1:5002/user/usuario.

También puedes utilizar herramientas como curl o aplicaciones como Postman para realizar solicitudes HTTP a los microservicios.