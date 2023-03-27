import random

class TableReservation:
    
    
    reservation_maked_persons = []
    customer_data = {'customer': [],
                     'table_name':(),
                     'table_number':()
                     }
    occupied_tables = {}
    free_tables = {}
     
    def get_table_for_customer(self, persons_amount: int) -> None:  # TODO: type anotation
        self.persons_amount = persons_amount
        appologise = f'Sorry we don`t have free table for you'  # You can wait? After some seconds ask again for reservation?
        if int(self.persons_amount) > 2:
            if not self.free_tables.get('family'):
                print(appologise)
            if len(self.free_tables.get('family')) != 0:
                return self.free_tables.get('family')
            
        if int(self.persons_amount) == 2:
            if not self.free_tables['double']:
                print(appologise)
            if len(self.free_tables['double']) != 0:
                return self.free_tables.get('double')
            if not self.free_tables['family']:
                print(appologise)
            if len(self.free_tables.get('family')) != 0:
                return self.free_tables.get('family')
            
        if persons_amount == 1:
            if not self.free_tables.get('single'):
                pass # FIXME:
            
            if len(self.free_tables.get('double')) != 0:
                return self.free_tables.get('double')
            if len(self.free_tables.get('family')) != 0:
                return self.free_tables.get('family')
            else:
                print(appologise)
            
                
    
    def check_person_name_for_reservation(self, customer_name: str)-> None:
        self.customer_name = customer_name
        
        self.generate_occupied_tables()
        table_name_random: str = random.choice(list(self.free_tables.keys()))  # Return random number of len dict.keys()
        table_random_number = random.choice(self.free_tables.get(table_name_random))
        
        table_assign = f"We assigned for you '{table_name_random}' table and number is '{table_random_number}'"
        
        if customer_name in self.reservation_maked_persons[::]:
            print(f"You name '{customer_name}' is on the reservation list. {table_assign} ")               
        else:
            self.customer_data['customer'] = customer_name
            print(f"You have not reserved a table. {table_assign}")
            
    
    def generate_occupied_tables(self): 
        
        type_of_tables: dict = {"single": [1, 2, 3],
                      "double": [4, 5, 6],
                      'family': [7, 8, 9]
                      }
        table_name_random = random.randint(0, len(list(type_of_tables.keys())))  # Return random number of len dict.keys()
        occupied_tables_list = list(type_of_tables.keys())[:(table_name_random)]
        
        for table_keys in type_of_tables.keys():
            table_number_random = random.randint(0, len(list(type_of_tables.values())))
            if table_keys in occupied_tables_list:
                number_of_occupied_tables = type_of_tables.get(table_keys)
                self.occupied_tables.update({table_keys: number_of_occupied_tables[:(table_number_random)]})
                if table_number_random < 3: # TODO: condition must to be from values lenght!
                    self.free_tables[table_keys] = number_of_occupied_tables[(table_number_random) - len(type_of_tables.values()): ]
            elif table_keys not in occupied_tables_list:
                self.free_tables.update({table_keys: type_of_tables.get(table_keys)})
        
      
def main():
    
    TableReservation.reservation_maked_persons=["Giedrius Kuprys", "Darius Kazimieras"]
    print(TableReservation.reservation_maked_persons)
    
    check_table = TableReservation()
    # Table reservation
    check_table.generate_occupied_tables()
    print(check_table.free_tables)  # DEL:
    customer = input('Please provide you full name for check reservation: ')
    perssons_amount = input('Good, for how many perssons need a table? ')
    print(check_table.get_table_for_customer(perssons_amount))
    #check_table.check_person_name_for_reservation(customer)
    
   


main()      