from flask import Blueprint, request
from bson.json_util import dumps
from flask_cors import CORS

from src.models.entities.Door import door
# utils
from src.utils import JsonMesage
from src.utils.script import scriptType

# Models
from src.models import DoorModel

main = Blueprint('door_blueprint', __name__)
CORS(main, origins='*')


@main.route('/', methods=['GET'], strict_slashes=False)
def get_doors():
    try:
        id_person = request.headers.get('Client')
        buzzers = DoorModel.get_doors(id_person)
        return dumps(buzzers)
    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/<id>', methods=['GET'])
def get_door(id):
    try:
        id_person = request.headers.get('Client')
        if DoorModel.door_exist(id_person, id):
            temp = DoorModel.get_door(id_person, id)
            return dumps(temp)
        else:
            return JsonMesage.message("Door dont exist")
    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/<id>', methods=['POST'])
def status_door(id):
    try:
        if request.json is None:
            return JsonMesage.message("Json empty")
        else:
            try:
                status = request.json["status"]
                id_person = request.headers.get('Client')
                if DoorModel.door_exist(id_person, id):
                    temp, status = scriptType.validate(status)
                    if temp:
                        DoorModel.post_door(id_person, id, status, id_person)
                        print("Validate")
                        return JsonMesage.message("Validate")  # Return "Validate" with a 200 OK status
                    else:
                        print("Invalid Status")
                        return JsonMesage.message(
                            "Invalid status")  # Return an error message with a 400 Bad Request status
                else:
                    return JsonMesage.message("Door dont exist")
            except Exception as ex:
                return JsonMesage.message_error(ex)
    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/add', methods=['POST'])
def add_door():
    try:
        if request.json is None:
            return JsonMesage.message("Json empty")
        else:
            try:
                id = request.json['id']
                ubication = request.json['ubication']
                status = 'False'
                database = request.json['database_id']
                id_person = request.headers.get('Client')

                temp = DoorModel.add_door(database, id_person, door(id, ubication, status, id_person))

                if temp:
                    return JsonMesage.message('Door created')
                else:
                    return JsonMesage.message('Door exist')

            except Exception as ex:
                return JsonMesage.message_error(ex)

    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/', methods=['DELETE'], strict_slashes=False)
def delete_door():
    try:
        if request.json is None:
            return JsonMesage.message("Json empty")
        else:
            try:
                id = request.json['id']
                database = request.json['database_id']
                id_person = request.headers.get('Client')

                temp = DoorModel.delete_door(database, id, id_person)

                if temp:
                    return JsonMesage.message('Door successfully delete')
                else:
                    return JsonMesage.message('Door dont exist')

            except Exception as ex:
                return JsonMesage.message_error(ex)
    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/', methods=['PUT'], strict_slashes=False)
def edit_door():
    try:
        if request.json is None:
            return JsonMesage.message("Json empty")
        else:
            try:
                id = request.json['id']
                database = request.json['database_id']
                id_person = request.headers.get('Client')

                temp = DoorModel.delete_door(database, id, id_person)

                if temp:
                    return JsonMesage.message('Door successfully delete')
                else:
                    return JsonMesage.message('Door dont exist')

            except Exception as ex:
                return JsonMesage.message_error(ex)
    except Exception as ex:
        return JsonMesage.message_error(ex)
