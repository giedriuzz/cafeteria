import logging
import logging.config
import time
from abc import ABC, abstractmethod
from typing import List, Optional, Union
from dataclasses import dataclass, field

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
logger = logging.getLogger("sLogger")


class TableReservationAbstract(ABC):
    @abstractmethod
    def get_time(self) -> tuple:
        pass


@dataclass
class Customer:
    """class for new customers."""

    full_name: str = ""
    reservation_time: str = ""
    qnt_of_persons: int = 0


@dataclass
class CafeteriaTables:
    """class for new table."""

    table_name: str = ""
    table_number: int = 0
    table_customer: list = field(default_factory=list)


@dataclass
class CustomerTableReservation:
    """class for working with tables, adding, reservations, customers."""

    tables_data: list = field(default_factory=list)
    temporary_customer_name = []

    @staticmethod
    def get_time() -> tuple:
        time_now = time.localtime()
        return time_now

    def current_time(self) -> str:
        assigned_time = time.strftime("%H:%m:%S", self.get_time())
        return assigned_time

    def add_table_to_list(self, *table_to_list: CafeteriaTables) -> None:
        """Add tables to tables_data list.
        Provide list of Objects for input.
        """
        for table in table_to_list:
            self.tables_data.append(table)

    def get_table_for_customer(self, customer: Customer) -> Optional[str]:
        """Get table for customer if table is free."""
        tables_data_gn = list(table for table in self.tables_data)
        for number, table in enumerate(tables_data_gn):
            reservation_msg = (
                f"{customer.full_name}, you table is: {table.table_number} "
                f"reserved at {customer.reservation_time} o`clock"
            )

            if not table.table_customer:
                if customer.qnt_of_persons >= 3:
                    if table.table_name == "Family":
                        self.tables_data[number].table_customer.append(customer)
                        return reservation_msg

                if customer.qnt_of_persons == 2:
                    if table.table_name == "Double" or table.table_name == "Family":
                        reserved_time = (t for t in table.table_customer)
                        print(*reserved_time)
                        self.tables_data[number].table_customer.append(customer)
                        return reservation_msg

                if customer.qnt_of_persons == 1:
                    if (
                        table.table_name == "Single"
                        or table.table_name == "Double"
                        or table.table_name == "Family"
                    ):
                        reserved_time = (t for t in table.table_customer)
                        print(*reserved_time)
                        self.tables_data[number].table_customer.append(customer)
                        return reservation_msg
            continue

        return f"Sorry we don`t have free tables for you"

    def check_customer_name(self, customer_name: Customer) -> Union[str, None]:
        print(f"Welcome to our restaurant , {customer_name.full_name}")
        print(f"Current time is: {self.current_time()}")
        self.temporary_customer_name.append(customer_name.full_name)
        find_customer = (z for z in self.tables_data if z.table_customer)
        for table in find_customer:
            # print(table)
            for name in table.table_customer:
                if name.full_name == customer_name.full_name:
                    self.temporary_customer_name.pop()
                    return (
                        f"{customer_name.full_name}, you table is: {table.table_number} "
                        f"reserved at {name.reservation_time} o`clock "
                    )

            continue
        else:
            print("You do not have a reservation")
            self.make_reservation()

    def make_reservation(self) -> None:
        reservation_time = input("Please enter time for reservation: ")
        number_of_quests = input("Please enter the number of guests: ")
        customer = Customer(
            full_name=self.temporary_customer_name[0],
            reservation_time=reservation_time,
            qnt_of_persons=int(number_of_quests),
        )
        self.temporary_customer_name.pop()
        print(self.get_table_for_customer(customer))


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

customer = Customer()
ahead_reservation_1 = Customer(
    full_name="Tadas Blinda", reservation_time="13", qnt_of_persons=3
)

add_table.get_table_for_customer(ahead_reservation_1)
# print(add_table.tables_data)
customer_full_name = input("Please provide your full name: ")
input_customer_name = Customer(full_name=customer_full_name)

print(add_table.check_customer_name(input_customer_name))
