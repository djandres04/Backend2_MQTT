from src.database.db import get_connection

from .entities.Temperature import Temperature

topic = "temp"


class TemperatureModel:
    def get_temp():
        try:
            client_db = get_connection("Temperature").find()
            return client_db
        except Exception as ex:
            raise ex

    def add_tempe(message):
        try:
            get_connection("Temperature").insert_one(Temperature(message).to_JSON())
        except Exception as ex:
            raise ex
