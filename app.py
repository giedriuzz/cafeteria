import connect
from main import MongoDb
from pymongo.collection import Collection


# mongo config
mongodb_host = "localhost"
mongodb_port = 27017
database_name = "tasks"
collection_name = "user_tasks"

mongo = MongoDb()
# connection
db = connect.connect_to_mongodb(mongodb_host, mongodb_port, database_name)
collection = db[collection_name]

from main import CafeteriaTables, CustomerTableReservation, Customer
import sys  #! #DEL only for debugging with launch.json argv

# Configuration of tables
table_1 = CafeteriaTables(table_name="Single", table_number=1, table_customer=[])
table_2 = CafeteriaTables(table_name="Single", table_number=2, table_customer=[])
table_3 = CafeteriaTables(table_name="Single", table_number=3, table_customer=[])
table_4 = CafeteriaTables(table_name="Double", table_number=4, table_customer=[])
table_5 = CafeteriaTables(table_name="Double", table_number=5, table_customer=[])
table_6 = CafeteriaTables(table_name="Double", table_number=6, table_customer=[])
table_7 = CafeteriaTables(table_name="Family", table_number=7, table_customer=[])
table_8 = CafeteriaTables(table_name="Family", table_number=8, table_customer=[])
table_9 = CafeteriaTables(table_name="Family", table_number=9, table_customer=[])

add_table = CustomerTableReservation()

add_table.add_table_to_list(
    table_1,
    table_2,
    table_3,
    table_4,
    table_5,
    table_6,
    table_7,
    table_8,
    table_9,
)


# ahead_reservation_customer_1 = Customer(
#     full_name="Tadas Blinda", reservation_time="13", qnt_of_persons=3
# )
# add_table.get_table_for_customer(ahead_reservation_customer_1)


print("Hello !")

input_full_name = input("Please provide your full name: ")
customer_full_name = Customer(full_name=input_full_name)
check_customer = add_table.check_customer(customer_full_name)


if check_customer is False:
    print("Sorry you don`t have a reservation, you can reserve now ")
    reservation_time = input("In what time do you want to reserve a table? ")
    qnt_of_customers = int(input("For how many people need a table? "))
    add_second_customer = Customer(
        full_name=input_full_name,
        reservation_time=reservation_time,
        qnt_of_persons=qnt_of_customers,
    )

    print(add_table.get_table_for_customer(add_second_customer))
    # print(add_table.tables_data)
else:
    print(
        f"{check_customer[0]}, you reserved before. You table number '{check_customer[1]}' and reservation time on {check_customer[2]} o`clock"  #! #type:ignore
    )
