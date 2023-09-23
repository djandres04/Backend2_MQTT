from database.db import get_connection

# Mosquitto
from src.mosquitto.src.buzzer import BuzzerMosquitto

from .entities.Buzzer import Buzzer

topic = "alarm"


class BuzzerModel():
    def get_buzzers():
        try:
            clientDb = get_connection("Devices").find({"topic": topic})
            return clientDb
        except Exception as ex:
            raise ex

    def get_buzzer(self, id):
        try:
            clientDb = get_connection("Devices").find({'topic': topic, "id": id})
            return clientDb
        except Exception as ex:
            raise ex

    def post_buzzer(id, status,person = None):
        try:
            #clientDb = get_connection("Devices")
            #historialDB = get_connection("History")
            #temp = {'topic': topic, "id": id}
            #time = clientDb.find_one(temp)["time_schedule"]

            """if time != waiting_time:
                clientDb.update_one(temp, {"$set": {"time_schedule": waiting_time}})
                BuzzerMosquitto.post_status()
                temp = clientDb.find_one(temp)
                buzzer = Buzzer(id,temp["ubication"],waiting_time,person)"""

            BuzzerMosquitto.post_status(id,status)
                #historialDB.insert_one(buzzer.to_JSON_person())

        except Exception as ex:
            raise ex