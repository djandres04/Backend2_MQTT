import json

import requests

from flask import jsonify

from decouple import config

topic = "alarm"

microservice_alarm = config("MICROSERVICE_ALARM")

headers = {'Content-Type': 'application/json'}


def get_alarms():
    try:
        response = requests.get(microservice_alarm+"/all")
        return response.json()
    except Exception as ex:
        print(str(ex))
        raise ex


def actives_alarms():
    try:
        response = requests.get(microservice_alarm)
        return response.json()
    except Exception as ex:
        print(str(ex))
        raise ex


def add_alarm(id_alarm, time, id_user=None):
    try:
        data = json.dumps({"id_alarm": id_alarm, "time_alarm": time, "person": id_user})
        response = requests.post(microservice_alarm+"/add", data=data, headers=headers)
        return response.json()
    except Exception as ex:
        raise ex


def delete_alarm(id_alarm, id_user):
    try:
        data = json.dumps({"id": id_alarm, "person": id_user})
        response = requests.delete(microservice_alarm + "/delete/" + id_alarm, data=data, headers=headers)
        return response.json()
    except Exception as ex:
        print(str(ex))
        raise ex
