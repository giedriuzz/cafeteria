# from pymongo.errors import ConnectionFailure, PyMongoError, ServerSelectionTimeoutError
from typing import Union
from dataclasses import dataclass
from datetime import datetime, date
from connect.connect_to_rpi import ConnectToMongoWithConfig
from main import QueryingDataBase

# from pymongo.operations import IndexModel


config_file = (
    "/home/giedrius/Documents/code_academy_projects/cafeteria/connect/config.json"
)
connection = ConnectToMongoWithConfig(config=config_file)
db = connection.get_uri_link()

customer_collection = QueryingDataBase(
    uri=db, db_name="cafeteria", collection_name="customer"
)
tables_collection = QueryingDataBase(
    uri=db, db_name="cafeteria", collection_name="tables"
)
meals_collection = QueryingDataBase(
    uri=db, db_name="cafeteria", collection_name="meals"
)
receipts_collection = QueryingDataBase(
    uri=db, db_name="cafeteria", collection_name="receipts"
)

# Strings pool
_say_name = "Please say your full name: "
_say_phone = "Please say your phone number: "
_say_reservation_day = "Please say preferred reservation day '2023-06-12':"
_say_reservation_hour = "Please say preferred reservation hour '14':"
_say_amount_of_persons = "Please say how many persons will be with you? "


@dataclass
class ClientCredentials:
    client_name: str
    client_phone_number: str


class Customer(ClientCredentials):
    def __init__(self, client: ClientCredentials) -> None:
        self.client = client

    def get_customer_id_by_name(self) -> str:
        customer = customer_collection.find_documents(
            field_name=self.client.client_name, value=self.client.client_phone_number
        )
        customer_id = [i["_id"] for i in customer]
        return str(customer_id[0])

    def get_time_stamp(self, date_str: str, hour_str: str) -> float:
        date_from_string = date_str + " " + hour_str
        new_dt = datetime.fromisoformat(date_from_string)
        return datetime.timestamp(new_dt)


def input_only_number(string: str) -> Union[int, str]:
    while True:
        try:
            integer = input(string)

            if integer.isdecimal() == True:
                return int(integer)
            else:
                raise ValueError
        except ValueError:
            print("! --- Wrong input, must to be a integer or float number --- !")
            continue


def input_only_string(string: str) -> str:
    while True:
        try:
            strings = input(string)
            if strings.replace(" ", "").isalpha() == True:
                return strings
            else:
                raise ValueError
        except ValueError:
            print("! --- Wrong input, must be a string --- !")
            continue


def input_customer_name_and_phone():
    customer_name = input_only_string(_say_name)
    customer_phone = input_only_number(_say_phone)
    return customer_name, customer_phone


def add_customer_to_db(user_name: str) -> bool:
    customer_phone = input_only_number(_say_phone)
    customer_collection.create_database_one_record(
        {"customer_name": user_name, "customer_phone": customer_phone}
    )
    return True


# *     PROGRAM STARTING FROM HERE      !


print("Welcome to our restaurant!", end="\n")
client_name = input_only_string(_say_name)
client_phone_number = str(input_only_number(_say_phone))
clients = ClientCredentials(
    client_name=client_name, client_phone_number=client_phone_number
)
customer = Customer(clients)

while True:
    client = customer_collection.find_one_document(
        field_name="client_name", value=clients.client_name
    )
    if client is not None:
        # [] function -> print the name, table number, reservation time
        print("You are here!")
    else:
        # [x] ask reservation time, day, hour
        # [x] ask how many persons will be
        # [] function -> get customer id
        # [] function -> search are free table
        # [] function -> write customer in table
        # [] function -> print the name, table number, reservation time
        reservation_day = input_only_number(_say_reservation_day)
        reservation_hour = input_only_number(_say_reservation_hour)
        amount_of_persons = input_only_number(_say_amount_of_persons)
        print(
            customer.get_time_stamp(date_str=reservation_day, hour_str=reservation_hour)
        )

        print("You are not here!")


# while True:
#     reserved_before = input_only_string(
#         "Do you was reserved before ? NO\YES\nYou answer:"
#     )
#     if reserved_before.lower() == "yes" or reserved_before == "y":
#         name = input_only_string(_say_name)
#         find_customer = customer_collection.find_documents(
#             field_name="customer_name", value=name
#         )
#         if find_customer:
#             print(name)
#         else:
#             print("Sorry we couldn't find you in our restaurant list")
#             add_customer_to_db(name)
#         break
#     else:
#         # add_customer_to_db(name)
#         break

# filtered = customer_collection.filter_fields(
#     fields={"customer_name": "Tadas Blinda"},
#     filters={"_id": 0},
# )
# print(filtered)


# print(
#     collection_customer.find_documents(field_name="customer_name", value=customer_name)
# )

# id = customer.get_customer_id_by_name(field_name="customer_name", value="Tadas Blinda")

# print(id)
# id_fnd = collection_customer.find_documents(field_name="_id", value=ObjectId(id))


# # print(f"finded : {id_fnd}")
# customer_1 = {"customer_name": "Bronius Morkūnas", "customer_phone": "+37012345678"}
# customer_2 = {"customer_name": "Česlovas Šikšnius", "customer_phone": "+37012345680"}
# customer_3 = {"customer_name": "Tadas Blinda", "customer_phone": "+374512345680"}
# customer_4 = {"customer_name": "Česlovas Šikšnius", "customer_phone": "+37011345680"}
# customer_5 = {"customer_name": "Romas Blinda", "customer_phone": "+374512345689"}
# customer_6 = {"customer_name": "Robertas Kalnius", "customer_phone": "+37011385680"}
# collection_customer.create_database_many_records(
#     [customer_1, customer_2, customer_3, customer_4, customer_5, customer_6]
# )

# collection_customer.delete_document({"customer_name": "Česlovas Šikšnius"})

# --->> Create tables in collection "tables"
# table_1 = {
#     "table_name": "single",
#     "table_number": "1",
#     "reservation_time": 0,
#     "customer_id": "",
# }
# table_2 = {
#     "table_name": "single",
#     "table_number": "2",
#     "reservation_time": 0,
#     "customer_id": "",
# }
# table_3 = {
#     "table_name": "single",
#     "table_number": "3",
#     "reservation_time": 0,
#     "customer_id": "",
# }
# table_4 = {
#     "table_name": "double",
#     "table_number": "4",
#     "reservation_time": 0,
#     "customer_id": "",
# }
# table_5 = {
#     "table_name": "double",
#     "table_number": "5",
#     "reservation_time": 0,
#     "customer_id": "",
# }
# table_6 = {
#     "table_name": "double",
#     "table_number": "6",
#     "reservation_time": 0,
#     "customer_id": "",
# }
# table_7 = {
#     "table_name": "family",
#     "table_number": "7",
#     "reservation_time": 0,
#     "customer_id": "",
# }
# table_8 = {
#     "table_name": "family",
#     "table_number": "8",
#     "reservation_time": 0,
#     "customer_id": "",
# }
# table_9 = {
#     "table_name": "family",
#     "table_number": "9",
#     "reservation_time": 0,
#     "customer_id": "",
# }
# collection_tables.create_database_many_records(
#     [table_1, table_2, table_3, table_4, table_5, table_6, table_7, table_8, table_9]
# )
