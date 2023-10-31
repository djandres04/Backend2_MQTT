from src.database.db import get_connection

from .entities.Temperature import Temperature

topic = "temperature"


def get_temp(databse_id):
    try:
        client_db = get_connection(databse_id, "Temperature").find()
        return client_db
    except Exception as ex:
        print(str(ex))
        raise ex


def add_tempe(database_id, message):
    try:
        get_connection(database_id, "Temperature").insert_one(Temperature(message).to_JSON())
    except Exception as ex:
        print(str(ex))
        raise ex
