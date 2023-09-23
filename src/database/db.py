from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from decouple import config


def get_connection(collection_db):
    try:
        return MongoClient(
            config('MONGO_HOST'),
            int(config('MONGO_PORT'))
        )[config('MONGO_DATABASE')][collection_db]
    except ConnectionFailure as ex:
        raise ex
