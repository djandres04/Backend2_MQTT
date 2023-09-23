from flask import Flask, request, jsonify

import paho.mqtt.client as mqtt

from config import config

from routes import Buzzer
from routes import Door
from routes import Lighting
from routes import Temperature

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    return msg.payload

if __name__  == '__main__':
    app.config.from_object(config['development'])

    client = mqtt.Client()
    client.connect(config('MOSQUITTO_SERVER'), int(config('MOSQUITTO_PORT')), int(config('MOSQUITTO_ALIVE')))
    client.subscribe(topic)

    app.register_blueprint(Temperature.main, url_prefix = '/temp')
    app.register_blueprint(Buzzer.main, url_prefix='/buzzer')
    app.register_blueprint(Door.main, url_prefix='/door')
    app.register_blueprint(Lighting.main, url_prefix='/light')
    
    app.run(host="0.0.0.0")