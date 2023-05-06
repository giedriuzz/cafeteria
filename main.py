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
        tables_data_gn = (table for table in self.tables_data)
        for number, table in enumerate(tables_data_gn):
            reservation_msg = (
                f"{customer.full_name}, you table is: {table.table_number} "
                f"reserved at {customer.reservation_time} o`clock"
            )

            if not table.table_customer:

                def get_time_from_reservation():
                    # reserved_time = (t for t in table.table_customer)
                    # print(*reserved_time)
                    # self.tables_data[number].table_customer.append(customer)
                    return reservation_msg

                if customer.qnt_of_persons >= 3:
                    if table.table_name == "Family":
                        self.tables_data[number].table_customer.append(customer)
                        get_time_from_reservation()
                        break

                if customer.qnt_of_persons == 2:
                    if table.table_name == "Double" or table.table_name == "Family":
                        get_time_from_reservation()
                        break
                if customer.qnt_of_persons == 1:
                    if (
                        table.table_name == "Single"
                        or table.table_name == "Double"
                        or table.table_name == "Family"
                    ):
                        get_time_from_reservation()
                        break
                continue

            return f"Sorry we don`t have free tables for you"

    def check_customer(self, customer_name: Customer) -> bool | Optional[tuple]:
        # print(
        #     f"Welcome to our restaurant , {customer_name.full_name}"
        # )  # ? DEL panaikinti
        # print(f"Current time is: {self.current_time()}")  # ? DEL panaikinti
        # self.temporary_customer_name.append(customer_name.full_name)
        # find_customer = (z for z in self.tables_data if not z.table_customer)
        find_customer = (z for z in self.tables_data if z.table_customer)
        if not find_customer:
            return False
        else:
            for table in find_customer:
                # print("table: ", table)
                for name in table.table_customer:
                    if name.full_name == customer_name.full_name:
                        # self.temporary_customer_name.pop()
                        # break
                        return (
                            True,
                            table.table_name,
                            table.table_number,
                            name.full_name,
                            name.reservation_time,
                        )
                    continue

                    # return (
                    #     f"{customer_name.full_name}, for you reserved '{table.table_name}' table number is '{table.table_number}' "
                    #     f"reserved at {name.reservation_time} o`clock "
                    # )

    # def make_reservation(self, customer: Customer) -> str | None:
    #     customer = Customer(
    #         full_name=customer.full_name,
    #         reservation_time=customer.reservation_time,
    #         qnt_of_persons=int(customer.qnt_of_persons),
    #     )
    #     self.temporary_customer_name.pop()
    #     return self.get_table_for_customer(customer)


if __name__ == "__main__":
    pass
