from pymongo import MongoClient

# If an error occurs with the database, it can show what the error is
from pymongo.errors import ConnectionFailure

# Constant declaration in the project for establishing a connection with the database
from decouple import config


# Connection to a database and a specific collection within it
def get_connection(collection_db):
    try:
        return MongoClient(
            config('MONGO_HOST'),
            int(config('MONGO_PORT'))
        )[config('MONGO_DATABASE')][collection_db]
    except ConnectionFailure:
        return "ConectionFail"
