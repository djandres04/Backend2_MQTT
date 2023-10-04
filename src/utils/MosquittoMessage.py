import paho.mqtt.client as mqtt
from decouple import config


def publish_message(message, topic) -> None:
    client = mqtt.Client()
    client.connect(config('MOSQUITTO_SERVER'), int(config('MOSQUITTO_PORT')), int(config('MOSQUITTO_ALIVE')))

    client.publish(topic, message)
    client.disconnect()
