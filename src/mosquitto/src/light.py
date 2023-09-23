from src.mosquitto.utils.message import message_mosquitto

class LightMosquitto():
    def get_message(self) -> None:
        print("oh")

    def post_status(id,message) -> None:
        message_mosquitto.publish_message(message,"light/"+id)