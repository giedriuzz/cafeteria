from abc import ABC, abstractmethod
import time
from typing import Optional
import logging
import logging.config

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
logger = logging.getLogger('sLogger')

class TableReservationAbstract(ABC):
    
    @abstractmethod
    def get_time(self) -> None:  # FIXME: None?
        pass
    
    @abstractmethod
    def tables(self) -> None:  # FIXME: None?
        pass
    
    @abstractmethod
    def final_reservation(self) -> None:  # FIXME: None?
        pass
    
    
class TableReservation(TableReservationAbstract):
    list_of_reserved_customers = ['G G']
    tables_data = {
            'single':{
                1:{'occupied': False, 'customers': [], 'occupied_time': []},
                2:{'occupied': False, 'customers': [], 'occupied_time': []},
                3:{'occupied': False, 'customers': [], 'occupied_time': []},
                },
            'double':{
                1:{'occupied': False, 'customers': [], 'occupied_time': []},
                2:{'occupied': False, 'customers': [], 'occupied_time': []},
                3:{'occupied': False, 'customers': [], 'occupied_time': []},
            },
            'family':{
                1:{'occupied': False, 'customers': [], 'occupied_time': []},
                2:{'occupied': False, 'customers': [], 'occupied_time': []},
                3:{'occupied': False, 'customers': [], 'occupied_time': []},
            }
        }

    def __init__(self, full_name: str) -> None:
        self.full_name = full_name
    
    def greeting_customer(self):
        return f'Welcome to our restaurant "Casablanca" {self.full_name}'

    def check_customer(self) -> bool:  # Check are a customer in list list_of_reserved_customers=[]
        if self.full_name in self.list_of_reserved_customers:
            return True
        else:
            return False
    
    def add_customer(self):  # TODO type anotations
        return self.list_of_reserved_customers.append(self.full_name)

    def add_reservation(self, reserved_time, persons_number):  # TODO užbaigti šią vietą
        self.reserved_time = reserved_time
        self.persons_number = persons_number
        pass
    
    
        

    
    @staticmethod
    def get_time():  # FIXME: -> None? Also need for generate time on recipe
        time_now = time.localtime()
        return time_now
    
    def assigned_time(self):
        assigned_time = time.strftime('%A %B %d  %H:%m:%S', self.get_time())
        return assigned_time
    
    def tables(
        self, table_name: str=' ',
        table_number: int=1,
        table_occupied: bool = False,
        table_customers: str = ' ',
        table_occupied_time: str = ' '
        ) -> dict:  # FIXME: None?

        self.table_name = table_name
        self.table_number = table_number
        self.table_occupied = table_occupied
        self.table_customers = table_customers
        self.table_occupied_time = table_occupied_time
        self.tables_data = {
            'single':{
                1:{'occupied': False, 'customers': [], 'occupied_time': []},
                2:{'occupied': False, 'customers': [], 'occupied_time': []},
                3:{'occupied': False, 'customers': [], 'occupied_time': []},
                },
            'double':{
                1:{'occupied': False, 'customers': [], 'occupied_time': []},
                2:{'occupied': False, 'customers': [], 'occupied_time': []},
                3:{'occupied': False, 'customers': [], 'occupied_time': []},
            },
            'family':{
                1:{'occupied': False, 'customers': [], 'occupied_time': []},
                2:{'occupied': False, 'customers': [], 'occupied_time': []},
                3:{'occupied': False, 'customers': [], 'occupied_time': []},
            }
        }
        
        logger.debug(f'tables() table_name={table_name}')  # DEL

        self.tables_data[self.table_name].update(
            {
                self.table_number:{
                    'occupied': self.table_occupied,
                    'customers': self.table_customers,
                    'occupied_time': self.table_occupied_time
                    }
                }
            )
        return self.tables_data
    
    def assign_table(self):
        if self.full_name is not self.tables_data.get(''):
            print('Yes')
    
    def final_reservation(self):  # FIXME -> None? Assign table and other data
        reservation_data = []
        reservation_data.append(self.full_name)
        
        return reservation_data


customer_full_name = input('Please provide your full name: ')
# customer_reservation_time = input('What time would you like to reserve a table?')  # FIXME string?
# customer_persons_quantity = input('How many people will be with you?')

customer = TableReservation(customer_full_name)
print(customer.check_customer())
customer_reserved_table = customer.tables(table_name='single', table_number=1, table_occupied=True)

print(customer.greeting_customer())  # Pasisveikinimas
if customer.check_customer() == False:
    customer.add_customer()
print(customer.assigned_time())
print(customer.final_reservation())
print(customer.tables_data)

    
    

    
    