from pymongo import MongoClient
from dataclasses import dataclass
import json
from typing import Any, MutableMapping
from pymongo.errors import PyMongoError, ConnectionFailure
from urllib.parse import quote_plus


class ConnectToMongoWithConfig:
    """class for making some manipulations with mongodb.
    first need push the configuration file in JSON format:
        {
            "user_name": "user_name",
            "user_passwd": "strong password",
            "host": "192.168.1.81" (ip_address)
            "port": "27017" (port)
        }
    JSON file can be stored where you want, just give a Relative Path:
        config_file = (
        "/home/user/Documents/code_academy_projects/cafeteria/connect/config.json"
    )"""

    def __init__(self, config: Any) -> None:
        with open(config, "r") as f:
            config = json.load(f)

        username = config.get("user_name")
        password = config.get("user_psswd")
        host = config.get("host")
        port = config.get("port")
        uri = "mongodb://%s:%s@%s:%s/" % (
            quote_plus(username),
            quote_plus(password),
            quote_plus(host),
            port,
        )
        self.client = MongoClient(uri)

    def get_uri_link(self) -> MongoClient:
        return self.client

    def drop_database(self, db_name: str) -> str:
        """function for drop database
        just add in function database name (db_name)"""
        try:
            self.client.drop_database(db_name)
            return f"Database dropped successfully!"
        except ConnectionFailure as e:
            return f"Connection failure: {str(e)}"
        except PyMongoError as e:
            return f"An error occurred: {str(e)}"

    def drop_collection(self, db_name: str, collection_name: str) -> str:
        """function for drop collection
        just add in the function collection name (db_name) and
        collection name (collection_name)"""
        try:
            data_base = self.client[db_name]
            data_base.drop_collection(collection_name)
            return f"Collection dropped successfully!"
        except ConnectionFailure as e:
            return f"Connection failure: {str(e)}"
        except PyMongoError as e:
            return f"An error occurred: {str(e)}"

    def define_schema_validation_rules(
        self, schema_json: Any, db_name: str, collection_name: str
    ) -> str:
        """function for define schema validation rules.
            JSON file can be stored where you want, just give a Relative Path:
            config_file = (
            "/home/user/Documents/code_academy_projects/cafeteria/connect/schema_json.json"
        )
        """
        with open(schema_json, "r") as f:
            schema_json = json.load(f)
        data_base = self.client[db_name]
        collection = data_base[collection_name]
        data_base.command("collMod", collection.name, schema_json)
        return f"Schema validation rules was successfully applied!"

    def create_unique_index(
        self,
        unique_field_name: str,
        number: int,
        unique_bool: bool,
        db_name: str,
        collection_name: str,
    ) -> MutableMapping:
        """function to create a unique index
        in function must to be given a unique field name,
        number and boolean=True or False also database name
        and collection name
        """
        data_base = self.client[db_name]
        collection = data_base[collection_name]
        collection.create_index([(unique_field_name, number)], unique=unique_bool)
        return collection.index_information()


if __name__ == "__main__":
    config_file = "/home/giedrius/Documents/code_academy_projects/cafeteria/connect/config.json"  #! #DEL all lines before production
    db = ConnectToMongoWithConfig(config_file)

    # print(db.drop_collection(db_name="test_db", collection_name="test"))

    # print(db.drop_database(db_name="test_db"))

    # print(
    #     db.create_unique_index(
    #         unique_field_name="price",
    #         number=1,
    #         unique_bool=True,
    #         db_name="pets",
    #         collection_name="new_party",
    #     )
    # )
    # print(db.drop_database(db_name="exercise_db"))
    # print(db.drop_collection(db_name="pets", collection_name="error"))
    # print(
    #     db.create_unique_index(
    #         unique_field_name="name",
    #         number=1,
    #         unique_bool=True,
    #         db_name="pets",
    #         collection_name="new_party",
    #     )
    # )
    # db = ConnectToMongoWithConfig(
    #     config=config_file, db_name="animals", collection_name="dogs"
    # ).connect_to_mongodb()
    # schema = CreateValidationSchema(base=db, collection_name="cafeteria")

    # # schema.create_unique_index(
    # #     unique_field_name="customer_phone", number=1, unique_bool=False
    # # )

    customer_config = "/home/giedrius/Documents/code_academy_projects/cafeteria/validation_schema/customer.json"
    print(
        db.define_schema_validation_rules(
            schema_json=customer_config, db_name="cafeteria", collection_name="customer"
        )
    )

    # # schema.drop_collection()
    # schema.drop_database("animals")
