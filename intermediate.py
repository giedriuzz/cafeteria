from typing import List, Dict, Optional, Union
from connect.connect_to_rpi import ConnectToMongoWithConfig
from main import QueryingDataBase

config_file = "config.json"
db_cafeteria = ConnectToMongoWithConfig.connect_to_mongodb(config_file)
collection_customer = QueryingDataBase(db_cafeteria, collection_name="customer")


class Customer:
    def search_customer(self, field_name: str, value: str) -> str:
        customer = collection_customer.find_documents(
            field_name=field_name, value=value
        )
        if not customer:
            return False
        else:
            return True

    def get_customer_id_by_name(
        self, field_name: str, value: str
    ) -> Union[List[Dict], None]:
        """Get customer _id and return plain string
        function(field_name='customer_name', value='Tadas Blinda')"""
        customer = collection_customer.find_documents(
            field_name=field_name, value=value
        )
        customer_id = [i["_id"] for i in customer]
        return str(customer_id[0])
