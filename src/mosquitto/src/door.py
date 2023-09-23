from src.mosquitto.utils.message import message_mosquitto

class DoorMosquitto():
    def get_message(id) -> None:
        message_mosquitto.subscribe_message("door/"+id)

    def post_status(id,message) -> None:
        message_mosquitto.publish_message(message,"door/"+id)

