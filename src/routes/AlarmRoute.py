import json
from flask import Blueprint, jsonify, request
from bson.json_util import dumps

# Models
from models import AlarmModel
# utils
from utils import JsonMesage
from utils.script import scriptType

main = Blueprint('buzzer_blueprint', __name__)


@main.route('/', methods=['GET'], strict_slashes=False)
def active_alarm():
    try:
        return AlarmModel.actives_alarms()
    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/all', methods=['GET'])
def get_alarms():
    try:
        return AlarmModel.get_alarms()
    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/add', methods=['POST'])
def add_alarm():
    try:
        if request.json is None:
            return JsonMesage.message("Json empty")
        else:
            try:
                data = request.json

                id_alarm = data.get("id_alarm")
                time = data.get("time_alarm")
                description = data.get("description")
                person = data.get("person")

                return AlarmModel.add_alarm(id_alarm, time, person)

            except Exception as ex:
                return JsonMesage.message_error(ex)

    except Exception as ex:
        return JsonMesage.message_error(ex)


@main.route('/<id>', methods=['DELETE'], strict_slashes=False)
def delete_alarm(id):
    try:
        data = request.json
        person = data.get("person")

        temp = AlarmModel.delete_alarm(id, person)

        return temp
    except Exception as ex:
        return JsonMesage.message_error(ex)

