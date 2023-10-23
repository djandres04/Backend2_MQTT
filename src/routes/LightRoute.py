import json
from flask import Blueprint, request
from bson.json_util import dumps
from flask_cors import CORS
# utils
from src.utils import JsonMesage
from src.utils.script import scriptType
# Models
from src.models import LightModel

from src.models.entities.Light import light

main = Blueprint('light_blueprint', __name__)
CORS(main, origins='*')


@main.route('/', methods=['GET'], strict_slashes=False)
def get_lights():
    try:
        id_person = request.headers.get('Client')
        temp = LightModel.get_lights(id_person)
        return dumps(temp)
    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/<id>', methods=['GET'])
def get_light(id):
    try:
        id_person = request.headers.get('Client')
        if LightModel.light_exist(id_person, id):
            temp = LightModel.get_light(id_person, id)
            return dumps(temp)
        else:
            return JsonMesage.message("Light dont exist")
    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/<id>', methods=['POST'])
def status_light(id):
    try:
        if request.json is None:
            return JsonMesage.message_error("Json empty")
        else:
            try:
                status = request.json["status"]
                id_person = request.headers.get('Client')
                if LightModel.light_exist(id_person, id):
                    temp, status = scriptType.validate(status)
                    if temp:
                        LightModel.status_light(id_person, id, status)
                        print("Validate")
                        return JsonMesage.message("Validate")  # Return "Validate" with a 200 OK status
                    else:
                        print("Invalid Status")
                        return JsonMesage.message("Invalid status")  # Return an error message with a 400 Bad Request status
                else:
                    return JsonMesage.message("Light dont exist")
            except Exception as ex:
                return JsonMesage.message_error(ex)
    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/add', methods=['POST'])
def add_light():
    try:
        if request.json is None:
            return JsonMesage.message_error("Json empty")
        else:
            try:
                id = request.json['id']
                ubication = request.json['ubication']
                status = 'False'
                database = request.json['database_id']
                id_person = request.headers.get('Client')

                temp = LightModel.add_light(database, light(id, ubication, status, id_person), id_person)

                if temp:
                    return JsonMesage.message('Light created')
                else:
                    return JsonMesage.message('Light exist')

            except Exception as ex:
                return JsonMesage.message_error(ex)

    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/', methods=['DELETE'])
def delete_light():
    try:
        if request.json is None:
            return JsonMesage.message_error("Json empty")
        else:
            try:
                id = request.json['id']
                database = request.json['database_id']
                id_person = request.headers.get('Client')

                temp = LightModel.delete_light(database, id, id_person)

                if temp:
                    return JsonMesage.message('Light sucesfully delete')
                else:
                    return JsonMesage.message('Light dont exist')

            except Exception as ex:
                return JsonMesage.message_error(ex)


    except Exception as ex:
        return JsonMesage.message_error(ex)
