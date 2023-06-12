# from pymongo.errors import ConnectionFailure, PyMongoError, ServerSelectionTimeoutError
from connect.connect_to_rpi import ConnectToMongoWithConfig
from main import QueryingDataBase

# from pymongo.operations import IndexModel
from intermediate import Customer


config_file = "config.json"
db_cafeteria = ConnectToMongoWithConfig.connect_to_mongodb(config_file)


collection_customer = QueryingDataBase(db_cafeteria, collection_name="customer")
collection_tables = QueryingDataBase(db_cafeteria, collection_name="tables")
collection_menu = QueryingDataBase(db_cafeteria, collection_name="dishes")
customer = Customer()


def input_customer_name_and_phone():
    customer_name = input("Please say your full name: ")
    customer_phone = input("Please say your phone number: ")
    return customer_name, customer_phone


print("Welcome to our restaurant!", end="\n")
while True:
    reserved_before = input("Do you was reserved before ?\nYES\nNO\n:").lower()
    if reserved_before == "yes" or reserved_before == "y":
        name = input_customer_name_and_phone()
        find_customer = customer.search_customer(
            field_name="customer_name", value=name[0]
        )
        print(find_customer)
        break
    else:
        name = input_customer_name_and_phone()
        add_customer = collection_customer.create_database_one_record(
            {"customer_name": name[0], "customer_phone": name[1]}
        )
        break


# print(
#     collection_customer.find_documents(field_name="customer_name", value=customer_name)
# )

# id = customer.get_customer_id_by_name(field_name="customer_name", value="Tadas Blinda")

# print(id)
# id_fnd = collection_customer.find_documents(field_name="_id", value=ObjectId(id))


# print(f"finded : {id_fnd}")
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
