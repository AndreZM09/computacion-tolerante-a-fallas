# Usa la imagen oficial de Node.js como base
FROM node:14

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copia los archivos de la aplicación al directorio de trabajo
COPY package*.json ./
COPY frontend ./frontend
COPY backend ./backend

# Instala las dependencias
RUN npm install

# Expone el puerto en el que la aplicación estará escuchando
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["node", "backend/server.js"]
