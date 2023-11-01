# Backend2_MQTT

## Descripción

Este es un proyecto de backend desarrollado en Python utilizando el marco de trabajo Flask y MQTT (Message Queuing Telemetry Transport). Este proyecto utiliza MongoDB como base de datos.

## Requisitos

- Python 3.8 o superior
- Flask 1.1.2 o superior
- Paho-MQTT 1.5.1 o superior
- MongoDB

## Configuración

Crea un archivo `.env` en el directorio raíz del proyecto con las siguientes variables de entorno:
```bash
SECRET_KEY = "your_secret_key"
MONGO_HOST = "your_mongo_ip"
MONGO_PORT = your_mongo_port
MONGO_USER = "your_mongo_user"
MONGO_PASS = "your_mongo_password"

MOSQUITTO_SERVER = "your_mqttbroker_ip"
MOSQUITTO_PORT = your_mqttbroker_port
MOSQUITTO_ALIVE = your_mqttbroker_live
```


Por favor, reemplaza `your_...` con tus valores reales.

## Instalación

Para instalar las dependencias necesarias para este proyecto, puedes usar pip:

```bash
pip install -r requirements.txt