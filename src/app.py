from flask import Flask, request, jsonify

# config
from config import config

# Routes
from routes import BuzzerRoute
from routes import DoorRoute
from routes import LightRoute
from routes import TemperatureRoute
from routes import MosquittoRoute

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


if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(MosquittoRoute.main, url_prefix='/mqtt')
    app.register_blueprint(TemperatureRoute.main, url_prefix='/temp')
    app.register_blueprint(BuzzerRoute.main, url_prefix='/buzzer')
    app.register_blueprint(DoorRoute.main, url_prefix='/door')
    app.register_blueprint(LightRoute.main, url_prefix='/light')

    app.run(host="0.0.0.0", port=5000, debug=True)
