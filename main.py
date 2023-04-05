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
    def final_reservation(self) -> None:  # FIXME: None?
        pass
    
    
class TableReservation(TableReservationAbstract):
    
    tables_data = {
            'single':{
                1:{'occupied': False, 'custtomers': ['aa aa'], 'occupied_time': [10, 12, 14, 16, 18, 20, 22]},
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

    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        
    def customer_full_name(self) -> str:
        full_name = self.name + ' ' + self.surname
        return full_name
    
    def greeting_customer(self):
        return f'{self.customer_full_name()}, welcome to our restoran "Casablanca" '
    
    @staticmethod
    def get_time():  # FIXME: -> None? Also need for generate time on recipe
        time_now = time.localtime()
        return time_now
    
    def assigned_time(self):
        assigned_time = time.strftime('%A %B %d  %H:%m:%S', self.get_time())
        return assigned_time
    
    def add_customer(self): # FIXME what of type anotation?
        
        #full_name = self.customer_full_name()
        for key in self.tables_data.keys():
            for n in range(1, len(self.tables_data.get(key, {}).values()) + 1):  # vietoj 'single' prasukti ciklą su kitais staliukais
                if len(occupied_time := self.tables_data.get(key, {}).get(n, {}).get('occupied_time', {})) < 8:
                    print(len(occupied_time))
                    self.tables_data[key][n]['custtomers'].append(self.customer_full_name())

        return self.tables_data

    def check_table(self):
        for key in self.tables_data.keys():
            for n in range(1, len(self.tables_data.get(key, {}).values()) + 1):  # vietoj 'single' prasukti ciklą su kitais staliukais
                if self.customer_full_name() in self.tables_data.get(key, {}).get(n, {}).get('custtomers', {}):
                    index_of_name: list = self.tables_data.get(key, {}).get(n, {}).get('custtomers', {})
                    print(index_of_name.index(self.customer_full_name()))
                else:
                    print('Nėra')

    def final_reservation(self):  # FIXME -> None? Assign table and other data
        reservation_data = []
        reservation_data.append(self.customer_full_name())
        
        return reservation_data


customer_name = input('Please input you name: ')
customer_surname = input('Please input you surname: ')
# customer_reservation_time = input('What time would you like to reserve a table?')  # FIXME string?
# customer_perssons_quantity = input('How many people will be with you?')

customer = TableReservation(name=customer_name, surname=customer_surname)

print(customer.add_customer())
print(customer.greeting_customer())
print(customer.assigned_time())


# print(customer.final_reservation())
#print(TableReservation.tables_data)

    
    

    
    