from connect.connect_to_rpi import ConnectToMongoWithConfig
from main import QueryingDataBase

config_file = "config.json"
db_cafeteria = ConnectToMongoWithConfig.connect_to_mongodb(config_file)
collection_customer = QueryingDataBase(db_cafeteria, collection_name="customer")


class Customer:
    def search_customer(self, field_name: str, value: str) -> str:
        a = collection_customer.find_documents(field_name=field_name, value=value)
        if not a:
            print("Customer arent in db!")
        else:
            print("Customer are in db!")
