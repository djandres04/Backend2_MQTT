from flask import Blueprint, request
from bson.json_util import dumps

# utils
from src.utils.JsonMesage import message_error
from src.utils.script import scriptType

# Models
from src.models.DoorModel import DoorModel

main = Blueprint('door_blueprint', __name__)


@main.route('/')
def get_doors():
    try:
        buzzers = DoorModel.get_doors()
        return dumps(buzzers)
    except Exception as ex:
        return message_error(ex)


@main.route('/<id>')
def get_door(id):
    try:
        door = DoorModel.get_door(id)
        return dumps(door)
    except Exception as ex:
        return message_error(ex)


@main.route('/<id>', methods=['POST'])
def status_door(id):
    if int(id) != 1:
        return "error", 400
    else:
        try:
            if request.json is not None:
                try:
                    # jsonLoad = json.loads(request.json)
                    # status = str(jsonLoad["status"])

                    # status = json_validate(request.get_json("status"), json.loads(request.json)["status"])

                    status = request.json.get("status", 'Vacio')

                    temp, status = scriptType.validate(status)

                    if temp:
                        DoorModel.post_door(id, status)
                        print("Validate")
                        return "Validate", 200  # Return "Validate" with a 200 OK status
                    else:
                        print("Invalid Status")
                        return "Invalid status", 400  # Return an error message with a 400 Bad Request status

                except Exception as ex:
                    message_error(ex)

        except Exception as ex:
            message_error(ex)
