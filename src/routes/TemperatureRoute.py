from flask import Blueprint, jsonify, request
from bson.json_util import dumps

# Models
from ..models import TemperatureModel

main = Blueprint('temperature_blueprint', __name__)


@main.route('/', methods=['GET'])
def get_temps():
    try:
        return dumps(TemperatureModel.get_temp())
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500