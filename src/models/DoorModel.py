from src.database.db import get_connection

# Mosquitto
from src.utils.MosquittoMessage import publish_message

from .entities.Door import Door

topic = "door"


class DoorModel:
    def get_doors():
        try:
            client_db = get_connection("Devices").find_one({"topic": topic})
            return client_db
        except Exception as ex:
            raise ex

    def post_door(id_device, status_request, person=None):
        try:
            # Obtain a connection to two collections: one for devices and the other for the historical
            # changes of device status
            client_db = get_connection("Devices")
            historical_db = get_connection("History")

            # The variable 'temp' is responsible for searching documents to be changed in the database
            temp = {'topic': topic, "id": id_device}

            # We can update the status of one device using 'update_one'
            client_db.update_one(temp, {"$set": {"status": status_request}})

            temp1 = client_db.find_one(temp)
            # For a better structure, we use the 'door' class to organize data
            door = Door(id_device, temp1["ubication"], status_request, person)

            # We use a method created in the 'door' class to convert data to JSON, which can then be inserted
            # into the 'history' collection
            historical_db.insert_one(door.to_JSON())

            # Lastly, we publish a message to its corresponding topic in order to instruct the device to change its
            # status
            publish_message(status_request, topic + "/" + id_device)

        except Exception as ex:
            raise ex

    def get_door(id_device):
        try:
            client_db = get_connection("Devices").find_one({'topic': topic, "id": id_device})
            return client_db
        except Exception as ex:
            raise ex
