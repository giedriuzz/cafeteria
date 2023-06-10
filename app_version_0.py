from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import ConnectionFailure, PyMongoError, ServerSelectionTimeoutError
import json
from connect.connect import ConnectToRpi4
from main import QueryingDataBase
from pymongo.operations import IndexModel


def connect_to_mongodb(config: str) -> MongoClient:
    """prisijungiama prie RPI"""
    try:
        with open(config, "r") as f:
            config = json.load(f)

        host = config.get("host")
        port = config.get("port")
        username = config.get("user_name")
        password = config.get("user_psswd")
        auth_source = config.get("database")
        # collection_name = config.get("collection")

        db = ConnectToRpi4(
            user_name=username,
            user_passwd=password,
            host=host,
            port=port,
            db_name=auth_source,
        )
        return db

    except PyMongoError as e:
        print("An error occurred:", str(e))
        return None


def find_user_by_name_and_phone(user_name: str, phone_number: str):
    pass


config_file = "config.json"
# Usage
db = connect_to_mongodb(config_file)


querying_customer = QueryingDataBase(db, collection_name="customer")
print(querying_customer.find_documents(field_name="user_name", value="Tadas Blinda"))

id = querying_customer.get_customer_id_by_name(field_name="user_name", value="Giedrius")

print(id)
user_1 = {"user_name": "Bronius Morkūnas", "user_phone": "+37012345678"}
user_2 = {"user_name": "Česlovas Šikšnius", "user_phone": "+37012345680"}
querying_customer.create_database_many_records([user_1, user_2])
