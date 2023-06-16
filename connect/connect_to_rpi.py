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
    db_name: str
    collection: str


class ConnectToMongoWithConfig:
    def __init__(self, config: json, db_name: str, collection_name: str) -> None:
        self.config = config
        self.db_name = db_name
        self.collection_name = collection_name

    def connect_to_mongodb(self) -> MongoClient:
        """prisijungiama prie RPI"""
        try:
            with open(self.config, "r") as f:
                config = json.load(f)

            username = config.get("user_name")
            password = config.get("user_psswd")
            host = config.get("host")
            port = config.get("port")

            db = MainRpiRemoteDb(
                user_name=username,
                user_passwd=password,
                host=host,
                port=port,
                db_name=self.db_name,
                collection=self.collection_name,
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
        self.collection_name = collection_name
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

    def drop_collection(self) -> bool:
        try:
            self.db.drop_collection(self.collection_name)
            return True
        except:
            return False

    def drop_database(self, db_name) -> bool:
        try:
            self.client.drop_database(db_name)
            return True
        except:
            return False


if __name__ == "__main__":
    config_file = (
        "/home/giedrius/Documents/code_academy_projects/cafeteria/connect/config.json"
    )
    db = ConnectToMongoWithConfig(
        config=config_file, db_name="animals", collection_name="dogs"
    ).connect_to_mongodb()
    schema = CreateValidationSchema(base=db, collection_name="cafeteria")

    # schema.create_unique_index(
    #     unique_field_name="customer_phone", number=1, unique_bool=False
    # )

    # customer_config = "/home/giedrius/Documents/code_academy_projects/cafeteria/validation_schema/customer.json"
    # print(schema.define_schema_validation_rules(customer_config))

    # schema.drop_collection()
    schema.drop_database("animals")
