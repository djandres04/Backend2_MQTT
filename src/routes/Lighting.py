import json
from flask import Blueprint, jsonify, request
from bson.json_util import dumps

# Models
from src.models.LightModel import LightModel

main = Blueprint('light_blueprint', __name__)


@main.route('/', methods=['GET'])
def get_lights():
    try:
        lights = LightModel.get_lights()
        return dumps(lights)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>', methods =['GET'])
def get_light(id):
    try:
        light = LightModel.get_light(id)
        return dumps(light)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>', methods = ['POST'])
def status_light(id):
    if int(id) >3:
        return "error", 400
    else:
        try:
            if request.json is not None:
                try:
                    #jsonload = json.loads(request.json)
                    #status = str(jsonload["status"])

                    status = request.json.get("status", 'Vacio')

                    if (status == "True") or (status == "False"):
                        LightModel.post_light(id, status)
                        print("Validate")
                        return "Validate", 200  # Return "Validate" with a 200 OK status
                    else:
                        print("Invalid Status")
                        return "Invalid status", 400  # Return an error message with a 400 Bad Request status
                except Exception as ex:
                    return jsonify({'message': str(ex)}), 500

        except Exception as ex:
            return jsonify({'message': str(ex)}), 500