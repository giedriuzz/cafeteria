from abc import ABC, abstractmethod
import time
from typing import Optional
import logging
import logging.config

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
logger = logging.getLogger('sLogger')

class TableReservationAbstract(ABC):
    
    @abstractmethod
    def customer_full_name(self, name: str, surname: str) -> str:
        pass
    
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
    
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        
    def customer_full_name(self) -> str:
        full_name = self.name + ' ' + self.surname
        return full_name
    
    def greeting_customer(self):
        return f'Welcome to our restoran "Casablanca" {self.customer_full_name()}'
    
    @staticmethod
    def get_time():  # FIXME: -> None? Also need for generate time on recipe
        time_now = time.localtime()
        return time_now
    
    def assigned_time(self):
        assigned_time = time.strftime('%A %B %d  %H:%m:%S', self.get_time())
        return assigned_time
    
    def tables(self, table_name: str=' ', table_number: int=1, table_occupied: bool=True) -> None:  # FIXME: None?
        self.table_name = table_name
        self.table_number = table_number
        self.table_occupied = table_occupied
        self.tables_data = {
            'single':{
                1:{'occupied': False, 'custtomers': [], 'occupied_time': []},
                2:{'occupied': False, 'custtomers': [], 'occupied_time': []},
                3:{'occupied': False, 'custtomers': [], 'occupied_time': []},
                },
            'double':{
                1:{'occupied': False, 'custtomers': [], 'occupied_time': []},
                2:{'occupied': False, 'custtomers': [], 'occupied_time': []},
                3:{'occupied': False, 'custtomers': [], 'occupied_time': []},
            },
            'family':{
                1:{'occupied': False, 'custtomers': [], 'occupied_time': []},
                2:{'occupied': False, 'custtomers': [], 'occupied_time': []},
                3:{'occupied': False, 'custtomers': [], 'occupied_time': []},
            }
        }
        
        logger.debug(f'tables() table_name={table_name}')
   
        self.tables_data[self.table_name].update({self.table_number:{'occupied': self.table_occupied}})
    
    def final_reservation(self):  # FIXME -> None? Assign table and other data
        reservation_data = []
        reservation_data.append(self.customer_full_name())
        
        return reservation_data


customer_name = input('Please input you name: ')
customer_surname = input('Please input you surname: ')
customer = TableReservation(name=customer_name, surname=customer_surname)
customer_reseved_table = customer.tables(table_name='single', table_number=1, table_occupied=True)


print(customer.greeting_customer())
print(customer.assigned_time())
print(customer.final_reservation())
print(customer.tables_data)

    
    

    
    