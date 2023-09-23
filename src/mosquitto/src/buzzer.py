from src.mosquitto.utils.message import message_mosquitto

class BuzzerMosquitto():
    def get_message(self) -> None:
        print("oh")

    def post_status(id,message) -> None:
        if message != "Vacio":
            message_mosquitto.publish_message(message,"buzzer/"+id)