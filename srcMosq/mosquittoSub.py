import paho.mqtt.client as mqtt
from decouple import config

from utils.topic import topic_process

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("sub/light/1")
    client.subscribe("sub/light/2")
    client.subscribe("sub/light/3")
    client.subscribe("sub/door/1")
    client.subscribe("sub/buzzer/1")
    client.subscribe("sub/tempe")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    temp = str(msg.payload)
    print(msg.topic+" "+temp)
    topic_process(msg.topic, temp)

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(config('MOSQUITTO_SERVER'), int(config('MOSQUITTO_PORT')), int(config('MOSQUITTO_ALIVE')))

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
except Exception as ex:
    print(str(ex))