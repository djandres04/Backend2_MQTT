from database.db import get_connection

#Mosquitto
from src.mosquitto.src.light import LightMosquitto

from .entities.Lighting import Light

topic = "light"

class LightModel():

    def get_lights():
        try:
            clientDb = get_connection("Devices").find({'topic':topic})
            return clientDb
        except Exception as ex:
            raise ex

    def get_light(id):
        try:
            clientDb = get_connection("Devices").find_one({'topic':topic,"id":id})
            return clientDb  
        except Exception as ex:
            raise ex

    def post_light(id, status_rquest,person =None):
        try:
            clientDb = get_connection("Devices")
            historialDB = get_connection("History")
            temp = {'topic': topic, "id": id}
            status = clientDb.find_one(temp)["status"]

            if status != status_rquest:
                clientDb.update_one(temp, {"$set": {"status": status_rquest}})
                LightMosquitto.post_status(id,status_rquest)
                temp1 = clientDb.find_one(temp)
                light = Light(id, temp1["ubication"],status_rquest,person)

                historialDB.insert_one(light.to_JSON_person())

        except Exception as ex:
            raise ex