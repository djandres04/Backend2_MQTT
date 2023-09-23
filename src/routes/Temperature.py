import json
from flask import Blueprint, jsonify, request
from bson.json_util import dumps

# Models
from src.models.TemperatureModel import TemperatureModel

main = Blueprint('temperature_blueprint', __name__)


@main.route('/', methods=['GET'])
def get_lights():
    try:
        return dumps(TemperatureModel.get_temp())
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/', methods = ['POST'])
def status_temp():
    try:
        temp = TemperatureModel.post_tempe(str("True"))
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500