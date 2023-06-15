from pymongo import MongoClient
from dataclasses import dataclass
import json
from pymongo.errors import PyMongoError, ConnectionFailure


@dataclass
class MainRpiRemoteDb:
    user_name: str
    user_passwd: str
    host: str
    port: int
    db_name: int


class ConnectToMongoWithConfig:
    def __init__(self, config: json) -> None:
        self.config = config

    def connect_to_mongodb(self) -> MongoClient:
        """prisijungiama prie RPI"""
        try:
            with open(self.config, "r") as f:
                config = json.load(f)

            host = config.get("host")
            port = config.get("port")
            username = config.get("user_name")
            password = config.get("user_psswd")
            auth_source = config.get("database")

            db = MainRpiRemoteDb(
                user_name=username,
                user_passwd=password,
                host=host,
                port=port,
                db_name=auth_source,
            )
            return db

        except ConnectionFailure as e:
            print("Connection failure:", str(e))
            return None
        except PyMongoError as e:
            print("An error occurred:", str(e))
            return None


class CreateValidationSchema(ConnectToMongoWithConfig):
    def __init__(self, base: MainRpiRemoteDb, collection_name: str):
        # self.base = base
        uri = "mongodb://%s:%s@%s:%s/" % (
            base.user_name,
            base.user_passwd,
            base.host,
            base.port,
        )
        self.db_name = base.db_name
        self.client = MongoClient(uri)
        self.db = self.client[base.db_name]
        self.collection = self.db[collection_name]

    def create_unique_index(
        self, unique_field_name: str, number: int, unique_bool: bool
    ) -> None:
        self.collection.create_index([(unique_field_name, number)], unique=unique_bool)

    def define_schema_validation_rules(self, schema_json: json):
        with open(schema_json, "r") as f:
            config = json.load(f)

        self.db.command("collMod", self.collection.name, config)


if __name__ == "__main__":
    config_file = (
        "/home/giedrius/Documents/code_academy_projects/cafeteria/connect/config.json"
    )
    db = ConnectToMongoWithConfig(config=config_file).connect_to_mongodb()
    schema = CreateValidationSchema(base=db, collection_name="customer")

    schema.create_unique_index(
        unique_field_name="customer_phone", number=1, unique_bool=True
    )
    customer_config = "/home/giedrius/Documents/code_academy_projects/cafeteria/validation_schema/customer.json"
    print(schema.define_schema_validation_rules(customer_config))
