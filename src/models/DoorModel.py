from database.db import get_connection

# Mosquitto
from utils.MosquittoMessage import publish_message

from models.entities.Door import door
from utils import ConverterTime

topic = "door"


def get_doors(database_id):
    try:
        client_db = get_connection(database_id, "Devices").find({"topic": topic})
        client_db.close()
        return client_db
    except Exception as ex:
        raise ex


def get_door(database_id, id_device):
    try:
        client_db = get_connection(database_id, "Devices").find_one({'topic': topic, "id": id_device})
        client_db.close()
        return client_db
    except Exception as ex:
        raise ex


def post_door(database_id, id_device, status_request, person=None):
    try:
        # Obtain a connection to two collections: one for devices and the other for the historical
        # changes of device status
        client_db = get_connection(database_id,  "Devices")
        historical_db = get_connection(database_id, "History")

        # The variable 'temp' is responsible for searching documents to be changed in the database
        temp = {'topic': topic, "id": id_device}

        # We can update the status of one device using 'update_one'
        client_db.update_one(temp, {"$set": {"status": status_request}})

        temp1 = client_db.find_one(temp)
        # For a better structure, we use the 'door' class to organize data
        door_temp = door(id_device, temp1["ubication"], status_request, person)

        # We use a method created in the 'door' class to convert data to JSON, which can then be inserted
        # into the 'history' collection
        historical_db.insert_one(door_temp.to_JSON())

        # Lastly, we publish a message to its corresponding topic in order to instruct the device to change its
        # status
        publish_message(status_request, topic + "/" + id_device)

        client_db.close()
        historical_db.close()

    except Exception as ex:
        raise ex


def add_door(database_id, id_user, door_temp):
    try:
        client_db = get_connection(database_id, "Devices")
        historical_db = get_connection(database_id, "History")

        temp_search = client_db.find_one({"id": door_temp.id, "topic": topic})

        if temp_search:
            return False
        else:
            door_object = door_temp.to_JSON()

            temp = {"object": door_object, "created_date": ConverterTime.time_now(), "create_person": id_user}

            historical_db.insert_one(temp)
            client_db.insert_one(door_object)

            client_db.close()
            historical_db.close()
            return True

    except Exception as ex:
        print(str(ex))
        raise ex


def delete_door(database_id, door_id, id_user):
    try:
        client_db = get_connection(database_id, "Devices")
        historical_db = get_connection(database_id, "History")

        temp_search = client_db.find_one({"id": door_id, "topic":topic})

        if temp_search:
            temp = {"object": temp_search, "delete_date": ConverterTime.time_now(), "delete_person": id_user}

            historical_db.insert_one(temp)
            client_db.delete_one({"id": door_id})

            client_db.close()
            historical_db.close()
            return True
        else:
            return False

    except Exception as ex:
        print(str(ex))
        raise ex


def door_exist(database_id, door_id):
    try:
        client_db = get_connection(database_id, "Devices")
        temp_search = client_db.find_one({"id": door_id})
        if temp_search is None:
            client_db.close()
            return False
        else:
            client_db.close()
            return True

    except Exception as ex:
        return str(ex)
