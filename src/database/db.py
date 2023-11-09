from pymongo import MongoClient

# If an error occurs with the database, it can show what the error is
from pymongo.errors import ConnectionFailure

# Constant declaration in the project for establishing a connection with the database
from decouple import config

# Obtén las variables de entorno
mongo_host = config('MONGO_HOST')
mongo_port = int(config('MONGO_PORT'))
mongo_username = config('MONGO_USER')
mongo_password = config('MONGO_PASS')


# Connection to a database and a specific collection within it
def get_connection(database_db, collection_db):
    try:
        return MongoClient(mongo_host, mongo_port, username=mongo_username, password=mongo_password)[database_db][
            collection_db]
    except ConnectionFailure as ex:
        raise ex
