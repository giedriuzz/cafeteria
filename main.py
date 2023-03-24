import random

class TableReservation:
    
    customer_data = []
    
    def check_table_availibility(self) -> tuple:
        type_of_tables: dict = {"single": 1,
                      "double": 2,
                      'family': 3
                      }
        check_table = random.choice(list(type_of_tables.items()))
        return check_table
    
    def ask_customer_name(self, customer_name=input('Please provide you full name: ')) -> str:
        self.customer_name: str = customer_name
        print(self.customer_name)
        
        
        
    


def main():
     print(TableReservation().check_table_availibility())
     
main()