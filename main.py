import datetime
import logging
import logging.config
import time
from abc import ABC, abstractmethod
from typing import List, Optional

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
logger = logging.getLogger("sLogger")


class TableReservationAbstract(ABC):
    @abstractmethod
    def get_time(self) -> None:  # FIXME: None?
        pass

    @abstractmethod
    def final_reservation(self) -> None:  # FIXME: None?
        pass


class TableReservation(TableReservationAbstract):
    list_of_reserved_customers = []
    free_tables_list = []  # List of free tables
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
            1: {"customers": []},
            2: {"customers": []},
            3: {"customers": []},
        },
    }

    def __init__(
        self, full_name: str = ""
    ) -> None:  # TODO time reservation type annotation change to vise versa List
        self.full_name = full_name

    def ahead_reservation(
        self,
        full_name_ahead: str,
        time_of_reservation_ahead: str,
        number_of_persons_ahead: int,
    ):
        self.full_name_ahead = full_name_ahead
        self.time_of_reservation_ahead = time_of_reservation_ahead
        self.number_of_persons_ahead = number_of_persons_ahead

    def greeting_customer(self) -> str:
        return f'Welcome to our restaurant "Casablanca" {self.full_name}'

    def check_customer(
        self,
    ) -> bool:  # [] Check are a customer in list list_of_reserved_customers=[]
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

    def get_free_tables_list(self) -> None:  # [x] done
        for i, x in self.tables_data.items():
            for z in x:
                if len(*self.tables_data[i].get(z).values()) == 0:
                    self.free_tables_list.append([i, z])

    def assign_table(
        self,
        full_name_ahead: str,
        time_of_reservation_ahead: str,
        number_of_persons_ahead: int,
    ) -> None:
        self.full_name_ahead = full_name_ahead
        self.time_of_reservation_ahead = time_of_reservation_ahead
        self.number_of_persons_ahead = number_of_persons_ahead

        if not self.free_tables_list:
            return f"Sorry, restaurant is full"

        if self.number_of_persons_ahead >= 3:
            for table in self.free_tables_list:
                if table[0] == "family":
                    return self.tables_data[table[0]][table[1]].update(
                        {
                            "customers": [
                                self.full_name_ahead,
                                self.time_of_reservation_ahead,
                                self.number_of_persons_ahead,
                            ]
                        }
                    )
                else:
                    return f"Sorry we don`t have a table for you"

        if self.number_of_persons_ahead >= 2:
            for table in self.free_tables_list:
                if table[0] == "double" or table[0] == "family":
                    return self.tables_data[table[0]][table[1]].update(
                        {
                            "customers": [
                                self.full_name_ahead,
                                self.time_of_reservation_ahead,
                                self.number_of_persons_ahead,
                            ]
                        }
                    )
                else:
                    return f"Sorry we don`t have a table for you"
        if self.number_of_persons_ahead >= 1:
            for table in self.free_tables_list:
                if table[0] == "single" or table[0] == "double" or table[0] == "family":
                    return self.tables_data[table[0]][table[1]].update(
                        {
                            "customers": [
                                self.full_name_ahead,
                                self.time_of_reservation_ahead,
                                self.number_of_persons_ahead,
                            ]
                        }
                    )
                else:
                    return f"Sorry we don`t have a table for you"

    def check_table_availability(self) -> int:
        """Patikrinti ar yra laisvų staliukų
        kiek bus svečių?
        pagal svečių kiekį imamas staliukas ar staliukai ir tikrinama
        gražiname staliuko pavadinimą su primtinu klientui vietų skaičiumi.."""
        pass

    def final_reservation(self):  # FIXME -> None? Assign table and other data
        reservation_data = []
        reservation_data.append(self.full_name)

        return reservation_data


reservation_ahead = TableReservation()
print(
    reservation_ahead.ahead_reservation(
        full_name_ahead="Giedrius Kuprys",
        time_of_reservation_ahead="10:00",
        number_of_persons_ahead=3,
    )
)

table = TableReservation()

customer_full_name = input("Please provide your full name: ")
# customer_reservation_time = input('What time would you like to reserve a table?')  # FIXME string?
# customer_persons_quantity = input('How many people will be with you?')
table.get_free_tables_list()
print(table.free_tables_list)
print(table.assign_table())
print(table.tables_data)

# print(new_reservation.check_customer())

# print(reservation_ahead.check_table_availability())

# print(reservation_ahead.greeting_customer())

# print(reservation_ahead.assigned_time())
# print(reservation_ahead.final_reservation())
# print(reservation_ahead.list_of_reserved_customers)
# # print(reservation_ahead.tables_data)
# print(reservation_ahead.free_table())
# print(reservation_ahead.free_tables)
