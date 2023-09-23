from src.database.db import get_connection

# Mosquitto
from src.mosquitto.src.door import DoorMosquitto

from .entities.Door import Door

topic = "door"

class DoorModel():
    def get_doors():
        try:
            clientDb = get_connection("Devices").find_one({"topic": topic})
            return clientDb
        except Exception as ex:
            raise ex

    def get_door(id):
        try:
            clientDb = get_connection("Devices").find_one({'topic': topic, "id": id})
            return clientDb
        except Exception as ex:
            raise ex

    def post_door(id,status_rquest,person = None):
        try:
            clientDb = get_connection("Devices")
            historialDB = get_connection("History")
            temp = {'topic': topic, "id": id}
            clientDb.update_one(temp,{"$set": {"status": status_rquest}})
            DoorMosquitto.post_status(id,status_rquest)
            temp1= clientDb.find_one(temp)
            door = Door(id,temp1["ubication"],status_rquest,person)

            historialDB.insert_one(door.to_JSON_person())

        except Exception as ex:
            raise ex
