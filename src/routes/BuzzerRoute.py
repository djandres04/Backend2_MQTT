import json
from flask import Blueprint, jsonify, request
from bson.json_util import dumps

# utils
from ..utils.JsonValidate import json_validate
# Models
from ..models.BuzzerModel import BuzzerModel

main = Blueprint('buzzer_blueprint', __name__)


@main.route('/', methods=['POST'])
def get_buzzers():
    try:
        buzzers = BuzzerModel.get_buzzers()
        return dumps(buzzers)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>', methods=['POST'])
def get_buzzer(id):
    try:
        buzzer = BuzzerModel.get_buzzer(id)
        return dumps(buzzer)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>', methods=['POST'])
def status_buzzer(id):
    if int(id) != 1:
        return "error", 400
    else:
        try:
            if request.json is not None:
                try:
                    # jsonload = json.loads(request.json)
                    # status = str(jsonload["status"])
                    status = json_validate(request.get_json("status"), str(json.loads(request.json)["status"]))

                    # status = request.json.get("status", 'Vacio')

                    if (status == "True") or (status == "False"):
                        BuzzerModel.post_buzzer(id, status)
                        print("Validate")
                        return "Validate", 200  # Return "Validate" with a 200 OK status
                    else:
                        print("Invalid Status")
                        return "Invalid status", 400  # Return an error message with a 400 Bad Request status
                except Exception as ex:
                    return jsonify({'message': str(ex)}), 500

        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
