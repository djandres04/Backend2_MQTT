from flask import Blueprint, request

from ..utils.script import scriptType
from ..utils.JsonMesage import message_error

from ..models import LightModel
from ..models import DoorModel
from ..models.BuzzerModel import BuzzerModel
from ..models import TemperatureModel

main = Blueprint('mqtt_blueprint', __name__)

database = "smartHome"


@main.route('/', methods=['POST'])
def mqtt_subscriber():
    if request.json is not None:
        try:
            temp = request.get_json()
            topic = temp.get("topic")
            if topic == 'light':
                temp, status = scriptType.validate(request.json["status"])
                if temp:
                    LightModel.post_light(database, request.json["id"], status)
                    return "Validate", 200  # Return "Validate" with a 200 OK status
                else:
                    return message_error("Error")

            if topic == 'door':
                temp, status = scriptType.validate(request.json["status"])
                if temp:
                    DoorModel.post_door(database,request.json["id"], status)
                    return "Validate", 200  # Return "Validate" with a 200 OK status
                else:
                    return message_error("Error")

            if topic == 'tempe':
                TemperatureModel.add_tempe(request.json["value"])
                return "Validate", 200  # Return "Validate" with a 200 OK status

            if topic == 'buzzer':
                temp, status = scriptType.validate(request.json["status"])
                if temp:
                    BuzzerModel.post_buzzer(request.json["id"], status)
                    return "Validate", 200  # Return "Validate" with a 200 OK status
                else:
                    return message_error("Error")

        except Exception as ex:
            print(str(ex))
            return message_error(str(ex))
    else:
        print("invalid")
        return message_error("Invalid")
