from typing import List, Dict, Optional, Union
from connect.connect_to_rpi import ConnectToMongoWithConfig
from main_for_delete import QueryingDataBase


class Customer:
    def search_customer(self, field_name: str, value: str) -> List[Dict]:
        customer = collection_customer.find_documents(
            field_name=field_name, value=value
        )
        return customer

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

    def get_customers_list_by_name(self, name: str) -> List[list]:
        names = {"customer_name": name}
        filters = {"_id": 0}
        filtered = collection_customer.filter_fields(fields=names, filters=filters)
        b = [[*i.values()] for i in filtered]
        return b


if __name__ == "__main__":
    # def search_customer(field_name: str, value: str) -> str:
    #     customer = collection_customer.find_documents(
    #         field_name=field_name, value=value
    #     )
    #     for customer in customer:
    #         print(customer)

    # search_customer(field_name="customer_name", value="Giedrius Kuprys")
    # search_customer(field_name="customer_name", value="Tadas Blinda")
    customer = Customer()
    list_of_same_documents = customer.get_customers_list_by_name(name="Giedrius Kuprys")
    for customer in enumerate(list_of_same_documents, 1):
        print(customer[1][1])
