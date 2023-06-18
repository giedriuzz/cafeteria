import logging
import logging.config
import time
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.results import InsertOneResult
from typing import Dict, List, Any, Optional, Union
from abc import ABC, abstractmethod
from typing import List, Literal, Optional, Union
from bson.objectid import ObjectId
from dataclasses import dataclass, field
from pymongo.errors import WriteError
from connect.connect_to_rpi import ConnectToMongoWithConfig


logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
logger = logging.getLogger("sLogger")


class QueryingDataBase:
    """Base class for querying of database"""

    def __init__(self, uri: MongoClient, db_name: str, collection_name: str) -> None:
        self.db_name = db_name
        self.client = uri
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_database_one_record(self, record: dict) -> str:
        """'Insert one record into database
        function({'name': record, 'value': record, 'type': record and etc})"""
        try:
            result = self.collection.insert_one(record)
            return str(result.inserted_id)
        except WriteError as e:
            return f"Not passed validation scheme one of fields! Error code: {e}"

    def create_database_many_records(self, record: Dict[str, Any]) -> str:
        """Create many records from list of dictionaries
        dict_1 = {name:value, etc}
        dict_2 = {name:value, etc}
        function([dict_1, dict_2]) or function([{name:value, etc}, {name:value, etc}])
        """
        result = self.collection.insert_many(record)
        return str(result.inserted_ids)

    def find_one_document(self, field_name: str, value: str) -> Union[dict, None]:
        """Find document in collection
        function(field_name='field_name', value='value') returns
        dict value or None"""
        query = {field_name: value}
        document = self.collection.find_one(query)
        return document

    def find_documents(self, field_name: str, value: str) -> List[Dict]:
        """Find documents in collection
        function(field_name='field_name', value='value') returns
        list of dictionaries"""
        query = {field_name: value}
        documents = self.collection.find(query)
        return list(documents)

    def update_one(self, query: Dict, update: Dict[str, Any]) -> int:
        result = self.collection.update_one(query, {"$set": update})
        return result.modified_count

    def update_many(self, query: Dict, update: Dict[str, Any]) -> int:
        result = self.collection.update_many(query, {"$set": update})
        return result.modified_count

    def delete_many_documents(self, collection: Collection, query: Dict) -> int:
        result = collection.delete_many(query)
        return result.deleted_count

    def delete_document(self, query: Dict) -> int:
        """Delete one document from the collection
        function({'name': 'Tadas})"""
        result = self.collection.delete_one(query)
        return result.deleted_count

    def filter_fields(self, fields: dict, filters: dict) -> List[dict]:
        db_fields = {**fields}
        filter = {**filters}
        result = self.collection.find(db_fields, filter)
        return list(result)


if __name__ == "__main__":
    config_file = (
        "/home/giedrius/Documents/code_academy_projects/cafeteria/connect/config.json"
    )
    db_uri = ConnectToMongoWithConfig(config_file).get_uri_link()

    collection_customer = QueryingDataBase(
        uri=db_uri, db_name="cafeteria", collection_name="customer"
    )

    print(
        collection_customer.create_database_one_record(
            {"client_name": "client", "client_phone_number": "12345678912345"}
        )
    )
    # collection_customer.delete_document({"client_name": "client"})
    # print(collection_customer.find_documents(field_name="client_name", value="client"))
    # print(
    #     collection_customer.find_one_document(field_name="client_name", value="client")
    # )

    # db = ConnectToRpi4(
    #     user_name="ufo",
    #     user_passwd="pempiai234",
    #     host="192.168.1.81",
    #     port=27017,
    #     db_name="cafeteria",
    #     collection_name="dishes",
    # )
    # cafeteria = CafeteriaDataBase(db)

    # db_1 = cafeteria.create_database_record(
    #     {
    #         "table_name": "Single",
    #         "table_number": 1,
    #         "reservation_time": "20203-06-07T23:00:00  +0000",
    #         "customer_id": "blabla",
    #     }
    # )
    # db_2 = cafeteria.create_database_record("")
    # task = CafeteriaDataBase(db)
    # print(task.find_documents(field_name="customer_name", value="customer"))
    # customer = cafeteria.create_database_record(
    #     {"user_name": "Giedrius", "phone_number": "+37066768789"}
    # )
    # tables = db .create_database_record(
    #     {
    #         "table_name": "Single",
    #         "table_number": 1,
    #         "reservation_time": "2023-06-06T00:00:00Z",
    #         "customer_id": "647e12a39b1bc7aa861dc1fd",
    #     }
    # )
    # dishes = cafeteria.create_database_record(
    #     {
    #         "dish_category": "vegetable",
    #         "dish_name": "cepelinai su varške",
    #         "dish_description": "cepeliniai is virtų bulvių su vargke",
    #         "dish_weight": 500,
    #         "preparation_time": 15,
    #         "dish_calories": 1034,
    #         "dish_price": 8.55,
    #         "customer_id": "647e12a39b1bc7aa861dc1fd",
    #     }
    # )
