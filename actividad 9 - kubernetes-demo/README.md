# Aplicación Node.js con Kubernetes

Esta es una aplicación simple de Node.js que responde con un saludo y el nombre del host del sistema.

## Requisitos

- [Node.js](https://nodejs.org/) instalado
- [Docker](https://www.docker.com/) instalado
- [Minikube](https://minikube.sigs.k8s.io/) instalado (para entornos locales de Kubernetes)

## Pasos para Ejecutar la Aplicación con Kubernetes

1. **Instalación de Dependencias:**
   ```bash
   npm install
    ```

2. **Construir la imagen de docker**
   ```bash
   docker build -t nombre-de-tu-imagen .
    ```

3. **Subir la Imagen a un Registro (Opcional):**
    Si planeas utilizar un registro de Docker diferente de Docker Hub, sube la imagen al registro.
   ```bash
   docker push nombre-de-tu-imagen
    ```

4. **Iniciar Minikube (para entornos locales):**
   ```bash
   minikube start
    ```

5. **Configurar kubectl para Usar Minikube**
   ```bash
   kubectl config use-context minikube
    ```
6. **Desplegar la Aplicación en Kubernetes:**
   ```bash
   kubectl apply -f kubernetes-deployment.yaml
    ```
    Asegúrate de tener un archivo kubernetes-deployment.yaml con la configuración de tu despliegue.

    Ejemplo de `kubernetes-deployment.yaml`
        apiVersion: apps/v1
        kind: Deployment
        metadata:
        name: nombre-de-tu-app
        spec:
        replicas: 1
        selector:
            matchLabels:
            app: nombre-de-tu-app
        template:
            metadata:
            labels:
                app: nombre-de-tu-app
            spec:
            containers:
            - name: nombre-de-tu-app
                image: nombre-de-tu-imagen:latest
                ports:
                - containerPort: 3000

7. **Exponer el Servicio:**
   ```bash
   kubectl expose deployment nombre-de-tu-app --type=NodePort --port=3000
    ```

8. **Obtener la URL del Servicio:**
   ```bash
   minikube service nombre-de-tu-app --url
    ```

9. **Acceder a la Aplicación:**
   ```bash
   kubectl apply -f kubernetes-deployment.yaml
    ```
