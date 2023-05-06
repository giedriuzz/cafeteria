from main import CafeteriaTables, CustomerTableReservation, Customer

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
reserve_table = CustomerTableReservation()
customer = Customer()
ahead_reservation_1 = Customer(
    full_name="Tadas Blinda", reservation_time="13", qnt_of_persons=3
)

add_table.get_table_for_customer(ahead_reservation_1)
# print(add_table.tables_data)
print("Hello !")
customer_full_name = input("Please provide your full name: ")
input_customer_name = Customer(full_name=customer_full_name)
check_customer = add_table.check_customer_name(input_customer_name)

if check_customer is False:
    print("Sorry you don`t have a reservation, you can reserve now ")
    reservation_time = input("In what time do you want to reserve a table? ")
    qnt_of_customers = int(input("For how many people need a table? "))
    reserve_table.make_reservation(
        reservation_time=reservation_time, number_of_quests=qnt_of_customers
    )
else:
    print(check_customer)
