from ..database.db import get_connection

# Mosquitto
from ..utils.MosquittoMessage import publish_message

from entities.Buzzer import Buzzer

topic = "alarm"


class BuzzerModel:
    def get_buzzer(id_device):
        try:
            client_db = get_connection("Devices").find({'topic': topic, "id": id_device})
            return client_db
        except Exception as ex:
            raise ex

    def get_buzzers():
        try:
            client_db = get_connection("Devices").find({"topic": topic})
            return client_db
        except Exception as ex:
            raise ex

    def post_buzzer(id_device, status_request, person=None):
        try:
            # clientDb = get_connection("Devices")
            # historialDB = get_connection("History")
            # temp = {'topic': topic, "id": id}
            # time = clientDb.find_one(temp)["time_schedule"]

            """if time != waiting_time:
                clientDb.update_one(temp, {"$set": {"time_schedule": waiting_time}})
                BuzzerMosquitto.post_status()
                temp = clientDb.find_one(temp)
                buzzer = Buzzer(id,temp["ubication"],waiting_time,person)"""

            publish_message(status_request, topic + "/" + id_device)
            # historialDB.insert_one(buzzer.to_JSON_person())

        except Exception as ex:
            raise ex