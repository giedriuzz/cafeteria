# from pymongo.errors import ConnectionFailure, PyMongoError, ServerSelectionTimeoutError
from typing import Union
from connect.connect_to_rpi import ConnectToMongoWithConfig
from main import QueryingDataBase

# from pymongo.operations import IndexModel
from intermediate import Customer


config_file = (
    "/home/giedrius/Documents/code_academy_projects/cafeteria/connect/config.json"
)
db_uri = ConnectToMongoWithConfig(config_file).get_uri_link()

collection_customer = QueryingDataBase(
    uri=db_uri, db_name="cafeteria", collection_name="customer"
)
# collection_tables = QueryingDataBase(db_cafeteria, collection_name="tables")
# collection_menu = QueryingDataBase(db_cafeteria, collection_name="dishes")
customer = Customer()

_say_name = "Please say your full name: "
_say_phone = "Please say your phone number: "


def input_customer_name_and_phone():
    customer_name = input_only_string(_say_name)
    customer_phone = input_only_number(_say_phone)
    return customer_name, customer_phone


def input_only_number(string: str) -> Union[int, str]:
    while True:
        try:
            integer = str(input(string))
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


def add_customer_to_db(user_name: str) -> bool:
    customer_phone = input_only_number(_say_phone)
    collection_customer.create_database_one_record(
        {"customer_name": user_name, "customer_phone": customer_phone}
    )
    return True


print("Welcome to our restaurant!", end="\n")
while True:
    reserved_before = input_only_string(
        "Do you was reserved before ? NO\YES\nYou answer:"
    )
    if reserved_before.lower() == "yes" or reserved_before == "y":
        name = input_only_string(_say_name)
        find_customer = customer.search_customer(field_name="customer_name", value=name)
        if find_customer:
            print(name)
        else:
            print("Sorry we couldn't find you in our restaurant list")
            add_customer_to_db(name)
        break
    else:
        # add_customer_to_db(name)
        break

filtered = collection_customer.filter_fields(
    fields={"customer_name": "Tadas Blinda"},
    filters={"_id": 0},
)
print(filtered)
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
