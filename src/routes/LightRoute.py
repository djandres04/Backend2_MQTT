import json
from flask import Blueprint, request
from bson.json_util import dumps

#utils
from src.utils.JsonMesage import message_error
from src.utils.script import scriptType
# Models
from src.models.LightModel import LightModel

main = Blueprint('light_blueprint', __name__)


@main.route('/', methods=['GET'])
def get_lights():
    try:
        lights = LightModel.get_lights()
        return dumps(lights)
    except Exception as ex:
        return message_error(ex)


@main.route('/<id>', methods =['GET'])
def get_light(id):
    try:
        light = LightModel.get_light(id)
        return dumps(light)
    except Exception as ex:
        return message_error(ex)


@main.route('/<id>', methods = ['POST'])
def status_light(id):
    if int(id) >3:
        return "error", 400
    else:
        try:

            if request.json is None:
                return message_error("Json empty")
            else:
                try:
                    status = request.json["status"]

                    temp, status = scriptType.validate(status)

                    if temp:
                        LightModel.post_light(id, status)
                        print("Validate")
                        return "Validate", 200  # Return "Validate" with a 200 OK status
                    else:
                        print("Invalid Status")
                        return "Invalid status", 400  # Return an error message with a 400 Bad Request status
                except Exception as ex:
                    return message_error(ex)

        except Exception as ex:
            return message_error(ex)

@main.route('/add',methods=['POST'])
def add_light():
    try:
        add_light
    except Exception as ex:
        return message_error(ex)