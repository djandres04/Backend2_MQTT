# Usar una imagen base de Python
FROM python:3.11.4-alpine

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

COPY . /app

# Instalar las dependencias de tu aplicación (si es necesario)
RUN pip install -r requirements.txt

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app/src

EXPOSE 5000

ENV PYTHONPATH app/src

# Especificar el comando para ejecutar tu aplicación
CMD ["python", "app.py"]