from bson.json_util import dumps

import requests
import json
import utils.toJSON as toJSON

from database.db import get_connection
from decouple import config


def data_tempe(topic, status):
    data_out = dumps(toJSON.to_json(topic,status))
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(config('SERVER_REST'),data=data_out, headers=headers)
        response_message(response)
    except Exception as ex:
        print(str(ex))
        get_connection("Temperature").insert_one(data_out)

def data_status(id, topic , status):
    data_out = dumps(toJSON.to_json(topic,status, id))
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(config('SERVER_REST'),data=data_out, headers=headers)
        response_message(response)
    except Exception  as ex:
        print(str(ex))
        get_connection("Devices").update_one({"topic":topic,"id":id}, {"$set": {"status":status}})

def data_buzzer(id, topic, status):
    data_out=dumps(toJSON.to_json(topic,status,id))
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(config('SERVER_REST'),json=data_out, headers=headers)
        response_message(response)
    except Exception  as ex:
        print(str(ex))
        get_connection("Buzzer").update_one({"topic":topic,"id":id}, {"$set": {"status":status}})

def response_message(response_in):
    if response_in.status_code == 200:
        print("Solicitud exitosa")
    else:
        print("Error en la solicitud:", response_in.status_code, response_in.text)