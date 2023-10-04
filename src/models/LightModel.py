from src.database.db import get_connection

# Mosquitto
from src.utils.MosquittoMessage import publish_message

from src.models.entities.Light import Light

topic = "light"


class LightModel:
    def get_lights():
        try:
            client_db = get_connection("Devices").find({'topic': topic})
            return client_db
        except Exception as ex:
            raise ex

    def get_light(id_device):
        try:
            client_db = get_connection("Devices").find_one({'topic': topic, "id": id_device})
            return client_db
        except Exception as ex:
            raise ex

    def post_light(id_device, status_request, person=None):
        try:

            # Obtain a connection to two collections: one for devices and the other for the historical
            # changes of device status
            client_db = get_connection("Devices")
            historical_db = get_connection("History")

            # The variable 'temp' is responsible for searching documents to be changed in the database
            temp = {'topic': topic, "id": id_device}

            # We can update the status of one device using 'update_one'
            client_db.update_one(temp, {"$set": {"status": status_request}})

            temp = client_db.find_one(temp)
            # For a better structure, we use the 'door' class to organize data
            light = Light(id_device, temp["ubication"], status_request, person)

            # We use a method created in the 'door' class to convert data to JSON, which can then be inserted
            # into the 'history' collection
            historical_db.insert_one(light.to_JSON())

            # Lastly, we publish a message to its corresponding topic in order to instruct the device to change its status
            publish_message(status_request, topic + "/" + id_device)

        except Exception as ex:
            raise ex
