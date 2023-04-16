from abc import ABC, abstractmethod
import time
from typing import List, Optional
import logging
import logging.config
import datetime

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
logger = logging.getLogger("sLogger")


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
    list_of_reserved_customers = ["G G"]
    tables_data = {
        "single": {
            1: {"customers": []},
            2: {"customers": []},
            3: {"customers": []},
        },
        "double": {
            1: {"customers": []},
            2: {"customers": []},
            3: {"customers": []},
        },
        "family": {
            1: {"customers": [["Giedrius Kuprys", "16:45"]]},
            2: {"customers": [["Tadas Blinda", "20:45"]]},
            3: {"customers": []},
        },
    }

    def __init__(
        self, full_name: str, time_of_reservation: List[int], number_of_persons: int
    ) -> None:
        self.full_name = full_name
        self.time_of_reservation = time_of_reservation
        self.number_of_persons = number_of_persons

    def greeting_customer(self):
        return f'Welcome to our restaurant "Casablanca" {self.full_name}'

    def check_customer(
        self,
    ) -> bool:  # Check are a customer in list list_of_reserved_customers=[]
        if self.full_name in self.list_of_reserved_customers:
            return True
        else:
            return False

    def add_customer(self) -> Optional[int]:  # TODO type annotations
        pass

    def add_reservation(
        self, reserved_time, persons_quantity
    ):  # TODO užbaigti šią vietą
        self.reserved_time = reserved_time
        self.persons_quantity = persons_quantity
        pass

    @staticmethod
    def get_time():  # FIXME: -> None? Also need for generate time on recipe
        time_now = time.localtime()
        return time_now

    def assigned_time(self):
        assigned_time = time.strftime("%A %B %d  %H:%m:%S", self.get_time())
        return assigned_time

    def tables(
        self,
        table_name: str = " ",
        table_number: int = 1,
        table_occupied: bool = False,
        table_customers: str = " ",
        table_occupied_time: str = " ",
    ) -> dict:  # FIXME: ištrinti?
        self.table_name = table_name
        self.table_number = table_number
        self.table_occupied = table_occupied
        self.table_customers = table_customers
        self.table_occupied_time = table_occupied_time
        self.tables_data = {
            "single": {
                1: {"occupied": False, "customers": [], "occupied_time": []},
                2: {"occupied": False, "customers": [], "occupied_time": []},
                3: {"occupied": False, "customers": [], "occupied_time": []},
            },
            "double": {
                1: {"occupied": False, "customers": [], "occupied_time": []},
                2: {"occupied": False, "customers": [], "occupied_time": []},
                3: {"occupied": False, "customers": [], "occupied_time": []},
            },
            "family": {
                1: {"occupied": False, "customers": [], "occupied_time": []},
                2: {"occupied": False, "customers": [], "occupied_time": []},
                3: {"occupied": False, "customers": [], "occupied_time": []},
            },
        }

        logger.debug(f"tables() table_name={table_name}")  # DEL

        self.tables_data[self.table_name].update(
            {
                self.table_number: {
                    "occupied": self.table_occupied,
                    "customers": self.table_customers,
                    "occupied_time": self.table_occupied_time,
                }
            }
        )
        return self.tables_data

    def assign_table(self):
        if self.full_name is not self.tables_data.get(""):
            print("Yes")

    def check_table_availability(self) -> int:
        """Patikrinti ar yra laisvų staliukų
            kiek bus svečių?
            pagal svečių kiekį imamas staliukas ar staliukai ir tikrinama
        gražiname staliuko pavadinimą su primtinu klientui vietų skaičiumi"""
        (number_of_persons_for_check := self.number_of_persons)
        if number_of_persons_for_check >= 3:
            # tikrinami 'family' staliuka.index(value)
            for x in self.tables_data["family"]:
                if len(self.tables_data["family"].get(x).get("customers")) >= 1:
                    continue
                return x

        if number_of_persons_for_check >= 1:
            # tikrinami visi staliukai 'single', 'double', 'family'
            pass

    def final_reservation(self):  # FIXME -> None? Assign table and other data
        reservation_data = []
        reservation_data.append(self.full_name)

        return reservation_data


reservation_ahead = TableReservation(
    full_name="Giedrius Kuprys", time_of_reservation=[16, 30], number_of_persons=3
)
print(reservation_ahead.greeting_customer())
customer_full_name = input("Please provide your full name: ")
# customer_reservation_time = input('What time would you like to reserve a table?')  # FIXME string?
# customer_persons_quantity = input('How many people will be with you?')


print(reservation_ahead.check_customer())
print(reservation_ahead.check_table_availability())

print(reservation_ahead.greeting_customer())
if reservation_ahead.check_customer() == False:
    reservation_ahead.add_customer()
print(reservation_ahead.assigned_time())
print(reservation_ahead.final_reservation())
print(reservation_ahead.list_of_reserved_customers)
print(reservation_ahead.tables_data)
