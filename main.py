import random

class TableReservation:
    
    
    reservation_maked_persons = []
    customer_data = {'customer': [],
                     'table_name':(),
                     'table_number':()
                     }
    
    def check_person_name_for_reservation(self):
        customer_name=input('Please provide you full name: ')
        if customer_name in self.reservation_maked_persons[::]:
            self.check_table_availibility()
            print(f"You name '{customer_name}' is on the reservation list. We assigned for you '{self.customer_data['table_name']}' table and number is '{self.customer_data['table_number']}'")
        else:
            self.customer_data['customer'] = customer_name
            self.check_table_availibility()
            print(f"We assigned for you '{self.customer_data['table_name']}' table and number is '{self.customer_data['table_number']}'")
            # print('We assigned for you table:', *[table for table in self.check_table_availibility()])
    
    def check_table_availibility(self) -> None: 
        type_of_tables: dict = {"single": [1, 2, 3],
                      "double": [4, 5, 6],
                      'family': [7, 8, 9]
                      }
        table_name = random.choice(list(type_of_tables.keys()))  # Return random table name
        table_number = random.choice(list(type_of_tables[table_name]))  # Return random number of random table name
        self.customer_data['table_name'] = table_name
        self.customer_data['table_number'] = table_number
        
    

    
        
        
def main():
    
    TableReservation.reservation_maked_persons=["Giedrius Kuprys", "Darius Kazimieras"]
    print(TableReservation.reservation_maked_persons)
    
    #print(', '.join(TableReservation.customer_data["customer"]))
    check_table = TableReservation()
    check_table.check_person_name_for_reservation()
    print(TableReservation.customer_data)
     


main()      
    