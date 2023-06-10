import logging
import logging.config
import time
from pymongo import MongoClient
from pymongo.collection import Collection, Cursor
from typing import Dict, List, Any, Optional, Union
from abc import ABC, abstractmethod
from typing import List, Literal, Optional, Union
from bson.objectid import ObjectId
from dataclasses import dataclass, field
from connect.connect import ConnectToRpi4


logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
logger = logging.getLogger("sLogger")


class QueryingDataBase:
    def __init__(self, base: ConnectToRpi4, collection_name: str) -> None:
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

    def create_database_one_record(self, record: list[dict]) -> str:
        result = self.collection.insert_one(record)
        return str(result.inserted_id)

    def create_database_many_records(self, record: Dict[str, Any]) -> str:
        """Create many records from list of dictionaries
        dict_1 = {name:value}
        dict_2 = {name:value}
        function([dict_1, dict_2]) or function([{name:value}, {name:value])"""
        result = self.collection.insert_many(record)
        return str(result.inserted_ids)

    def find_documents(self, field_name: str, value: str) -> List[Dict]:
        query = {field_name: value}
        documents = self.collection.find(query)
        return list(documents)

    def get_customer_id_by_name(self, field_name: str, value: str) -> List[Dict]:
        query = {field_name: value}
        documents = self.collection.find(query, {"_id": 1})
        customer_id = [i["_id"] for i in documents]
        return str(customer_id)

    def update_one(self, query: Dict, update: Dict[str, Any]) -> int:
        result = self.collection.update_one(query, {"$set": update})
        return result.modified_count

    def update_many(self, query: Dict, update: Dict[str, Any]) -> int:
        result = self.collection.update_many(query, {"$set": update})
        return result.modified_count

    def delete_documents(collection: Collection, query: Dict) -> int:
        result = collection.delete_many(query)
        return result.deleted_count

    def delete_documents(collection: Collection, query: Dict) -> int:
        result = collection.delete_one(query)
        return result.deleted_count


class TableReservationAbstract(ABC):
    @abstractmethod
    def get_time(self) -> tuple:
        pass


@dataclass
class Customer:
    """class for new customers."""

    full_name: str = ""
    reservation_time: str = ""
    qnt_of_persons: int = 0


@dataclass
class CafeteriaTables:
    """class for new table."""

    table_name: str = ""
    table_number: int = 0
    table_customer: list = field(default_factory=list)


@dataclass
class CustomerTableReservation:
    """class for working with tables, adding, reservations, customers."""

    tables_data: list = field(default_factory=list)
    temporary_customer_name = []

    @staticmethod
    def get_time() -> tuple:
        time_now = time.localtime()
        return time_now

    def current_time(self) -> str:
        assigned_time = time.strftime("%H:%m:%S", self.get_time())
        return assigned_time

    def add_table_to_list(self, *table_to_list: CafeteriaTables) -> None:
        """Add tables to tables_data list.
        Provide list of Objects for input.
        """
        for table in table_to_list:
            self.tables_data.append(table)

    def get_table_for_customer(self, customer: Customer) -> Optional[str]:
        """Get table for customer if table is free."""
        tables_data_list = [
            table for table in self.tables_data if not table.table_customer
        ]
        for number, table in enumerate(tables_data_list):
            reservation_msg = (
                f"{customer.full_name}, you table is: {table.table_number} "
                f"reserved at {customer.reservation_time} o`clock"
            )
            if tables_data_list:

                def get_time_from_reservation():
                    self.tables_data[number].table_customer.append(customer)
                    return reservation_msg

                if customer.qnt_of_persons >= 3:
                    if table.table_name == "Family":
                        get_time_from_reservation()
                        break

                if customer.qnt_of_persons == 2:
                    if table.table_name == "Double" or table.table_name == "Family":
                        get_time_from_reservation()
                        break

                if customer.qnt_of_persons == 1:
                    if (
                        table.table_name == "Single"
                        or table.table_name == "Double"
                        or table.table_name == "Family"
                    ):
                        get_time_from_reservation()
                        break
                continue
            return f"Sorry we don`t have free tables for you"

    def check_customer(self, customer_name: Customer) -> bool | Optional[tuple]:
        find_customer = [z for z in self.tables_data if z.table_customer]
        if not find_customer:
            return False
        else:
            for table in find_customer:
                for name in table.table_customer:
                    if name.full_name == customer_name.full_name:
                        return name.full_name, table.table_number, name.reservation_time
                    else:
                        return False


if __name__ == "__main__":
    db = ConnectToRpi4(
        user_name="ufo",
        user_passwd="pempiai234",
        host="192.168.1.81",
        port=27017,
        db_name="cafeteria",
        collection_name="dishes",
    )
    cafeteria = CafeteriaDataBase(db)

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
    # tables = cafeteria.create_database_record(
    #     {
    #         "table_name": "Single",
    #         "table_number": 1,
    #         "reservation_time": "2023-06-06T00:00:00Z",
    #         "customer_id": "647e12a39b1bc7aa861dc1fd",
    #     }
    # # )
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
