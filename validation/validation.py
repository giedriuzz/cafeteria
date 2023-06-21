from datetime import datetime
from typing import Union, Optional


class Validation:
    def input_only_number(self, string: str) -> int:
        while True:
            try:
                integer = input(string)

                if integer.isdecimal() == True:
                    return int(integer)
                else:
                    raise ValueError
            except ValueError:
                print("! --- Wrong input, must to be a integer or float number --- !")
                continue

    def input_only_phone_number(self, string: str) -> Union[int, str]:
        while True:
            try:
                integer = input(string)

                if integer.isdecimal() == True:
                    length = len(integer)
                    if length >= 9 and length <= 13:
                        return int(integer)
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print(
                    "! --- Wrong input, must to be a integer and length >= 9 or <= 13   --- !"
                )
                continue

    def input_only_string(self, string: str) -> str:
        while True:
            try:
                strings = input(string)
                if strings.replace(" ", "").isalpha() == True:
                    return strings
                else:
                    raise ValueError
            except ValueError:
                print("! --- Wrong input, must be a string --- !")
                continue

    def input_only_date(self, string: str) -> datetime:
        while True:
            try:
                date_example = "%Y-%m-%d"
                input_date = input(string)
                date = datetime.strptime(input_date, date_example)
                return date
            except ValueError:
                print("Date format must to be like '2023-01-23' !")
                continue

    def input_only_time(self, string: str) -> datetime:
        while True:
            try:
                date_example = "%H:%M"
                input_date = input(string)
                date = datetime.strptime(input_date, date_example)
                return date
            except ValueError:
                print("Time format must to be like '14:00' !")
                continue

    def less_then_seven(self, string: str) -> int | str:
        while True:
            try:
                integer = input(string)

                if integer.isdecimal() == True:
                    length = len(integer)
                    if length <= 7:
                        return int(integer)
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print(
                    "! --- Wrong input, we can serve table only for 7 persons   --- !"
                )
                continue

    def reduce_to_three(self, amount_of_persons: int) -> int:
        if amount_of_persons > 3:
            return 3
        else:
            return 3


if __name__ == "__main__":
    pass
    # print(Validation().decrease_integer_to_three(123))

    # def input_customer_name_and_phone(self):
    #     customer_name = self.input_only_string(_say_name)
    #     customer_phone = self.input_only_number(_say_phone)
    #     return customer_name, customer_phone
