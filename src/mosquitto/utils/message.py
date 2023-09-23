import paho.mqtt.client as mqtt
from decouple import config

class message_mosquitto():

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("%s/%s",)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        return msg.payload

    def subscribe_message(topic)->None:
        client = mqtt.Client()
        client.connect(config('MOSQUITTO_SERVER'), int(config('MOSQUITTO_PORT')), int(config('MOSQUITTO_ALIVE')))
        client.subscribe(topic)
    def publish_message(message, topic)->None:
        client = mqtt.Client()
        client.connect(config('MOSQUITTO_SERVER'),int(config('MOSQUITTO_PORT')),int(config('MOSQUITTO_ALIVE')))

        client.publish(topic,message)
        client.disconnect()
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.