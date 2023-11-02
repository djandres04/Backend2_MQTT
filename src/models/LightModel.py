from ..database.db import get_connection

# Mosquitto
from ..utils.MosquittoMessage import publish_message

from ..models.entities.Light import light

from ..utils import ConverterTime

topic = "light"


def get_lights(database_id):
    try:
        client_db = get_connection(database_id, "Devices").find({'topic': topic})
        return client_db
    except Exception as ex:
        raise ex


def get_light(database_id, id_device):
    try:
        client_db = get_connection(database_id, "Devices").find_one({'topic': topic, "id": id_device})
        return client_db
    except Exception as ex:
        raise ex


def post_light(database_id, id_device, status_request, person=None):
    try:
        # Obtain a connection to two collections: one for devices and the other for the historical
        # changes of device status
        client_db = get_connection(database_id, "Devices")
        historical_db = get_connection(database_id, "History")

        # The variable 'temp' is responsible for searching documents to be changed in the database
        temp = {'topic': topic, "id": id_device}

        # We can update the status of one device using 'update_one'
        client_db.update_one(temp, {"$set": {"status": status_request}})

        temp = client_db.find_one(temp)
        # For a better structure, we use the 'light' class to organize data
        light_temp = light(id_device, temp["ubication"], status_request, person)

        # We use a method created in the 'door' class to convert data to JSON, which can then be inserted
        # into the 'history' collection
        historical_db.insert_one(light_temp.to_JSON())

        # Lastly, we publish a message to its corresponding topic in order to instruct the device to change its status
        publish_message(status_request, topic + "/" + id_device)

    except Exception as ex:
        raise ex


def add_light(database_id, light_temp, id_user):
    try:
        client_db = get_connection(database_id, "Devices")
        historical_db = get_connection(database_id, "History")
        temp_search = client_db.find_one({"id": light_temp.id, "topic": topic})
        if temp_search:
            return False
        else:
            light_object = light_temp.to_JSON()
            temp = {"object": light_object, "created_date": ConverterTime.time_now(), "create_person": id_user}
            historical_db.insert_one(temp)
            client_db.insert_one(light_object)
            return True

    except Exception as ex:
        print(str(ex))
        raise ex


def delete_light(database_id, light_id, id_user):
    try:
        client_db = get_connection(database_id, "Devices")
        historical_db = get_connection(database_id, "History")

        temp_search = client_db.find_one({"id": light_id, "topic":topic})

        if temp_search:

            temp = {"object": temp_search, "delete_date": ConverterTime.time_now(), "delete_person": id_user}
            historical_db.insert_one(temp)

            client_db.delete_one({"id": light_id})
            return True
        else:
            return False

    except Exception as ex:
        print(str(ex))
        raise ex


def light_exist(database_id, light_id):
    try:
        client_db = get_connection(database_id, "Devices")
        temp_search = client_db.find_one({"id": light_id})
        if temp_search is None:
            return False
        else:
            return True

    except Exception as ex:
        return str(ex)
