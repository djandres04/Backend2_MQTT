import json

from flask import Blueprint, jsonify, request
from bson.json_util import dumps

# Models
from src.models.DoorModel import DoorModel

main = Blueprint('door_blueprint', __name__)


@main.route('/')
def get_doors():
    try:
        buzzers = DoorModel.get_doors()
        return dumps(buzzers)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_door(id):
    try:
        door = DoorModel.get_door(id)
        return dumps(door)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>', methods=['POST'])
def status_door(id):
    if int(id) != 1:
        return "error", 400
    else:
        try:
            if request.json is not None:
                try:
                    #jsonLoad = json.loads(request.json)
                    #status = str(jsonLoad["status"])

                    status = request.json.get("status", 'Vacio')

                    if (status == "True") or (status == "False"):
                        DoorModel.post_door(id, status)
                        print("Validate")
                        return "Validate", 200  # Return "Validate" with a 200 OK status
                    else:
                        print("Invalid Status")
                        return "Invalid status", 400  # Return an error message with a 400 Bad Request status

                    # status = request.json.get("status", 'Vacio')
                except Exception as ex:
                    return jsonify({'message': str(ex)}), 500

        except Exception as ex:
            return jsonify({'message': str(ex)}), 500