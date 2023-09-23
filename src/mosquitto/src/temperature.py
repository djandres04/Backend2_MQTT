import paho.mqtt.client as mqtt
from decouple import config

topicget = "TempOut"
topicpost = "TempGet"
class TemperatureMosquitto():
    def on_message(client, userdata, msg):
        print(msg.payload)
        return msg.payload

    def post_status(message) -> None:
        client = mqtt.Client()
        client.connect(config('MOSQUITTO_SERVER'), int(config('MOSQUITTO_PORT')), int(config('MOSQUITTO_ALIVE')))
        client.subscribe(topicget)
        client.publish(topicpost, message)
