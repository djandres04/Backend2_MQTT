# Usar una imagen base de Python
FROM python:3.11.4

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar git (si no está presente en la imagen base)
RUN apt-get update && apt-get install -y git

# Clonar el repositorio de GitHub
RUN git clone https://github.com/djandres04/Backend1.git

WORKDIR /app/Backend1

RUN git pull

# Instalar las dependencias de tu aplicación (si es necesario)
RUN pip install -r requirements.txt

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Especificar el comando para ejecutar tu aplicación
CMD ["python", "app.py"]