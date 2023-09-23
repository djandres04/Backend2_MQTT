from src.database.db import get_connection

#Mosquitto
from src.mosquitto.src.temperature import TemperatureMosquitto

from .entities.Temperature import Temperature

topic = "temp"

class TemperatureModel():

    def get_temp():
        try:
            clientDb = get_connection("Devices").find({'topic':topic})
            return clientDb
        except Exception as ex:
            raise ex

    def post_tempe(message,person =None):
        try:
            clientDb = get_connection("Devices").find_one({'topic':'temp'})
            historialDB = get_connection("History")
            tempera = TemperatureMosquitto.post_status(message)
            tempe = Temperature(clientDb["id"], clientDb["ubication"],tempera,person)

            historialDB.insert_one(tempe.to_JSON_person())

            return tempera
        except Exception as ex:
            raise ex