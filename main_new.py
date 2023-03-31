from abc import ABC, abstractmethod
import time
from typing import Optional

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
    
    def tables(self) -> None:  # FIXME: None?
        pass
    
    def final_reservation(self):  # FIXME -> None? Assign table and other data
        reservation_data = []
        reservation_data.append(self.customer_full_name())
        
        return reservation_data

customer_name = input('Please input you name: ')
customer_surname = input('Please input you surname: ')   
customer = TableReservation(name=customer_name, surname=customer_surname)

print(customer.greeting_customer())
print(customer.assigned_time())
print(customer.final_reservation())

    
    

    
    