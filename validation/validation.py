from datetime import datetime
from typing import Union


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
                print("Date format must to be like 'yyyy-mm-dd' !")
                continue

    def input_only_time(self, string: str) -> datetime:
        while True:
            try:
                date_example = "%H:%M"
                input_time = input(string)
                date = datetime.strptime(input_time, date_example)
                return date
            except ValueError:
                print("Time format must to be like 'hh:mm' !")
                continue

    def time_not_less_than_now(self, string: str, date: datetime) -> datetime:
        while True:
            try:
                time = self.input_only_time(string)
                format_time = datetime.strftime(time, "%H:%M")
                datetime_from_format_time = datetime.strptime(format_time, "%H:%M")
                time_now = datetime.now().replace(second=0, microsecond=0)
                time_adjusted = datetime(
                    year=date.year,
                    month=date.month,
                    day=date.day,
                    hour=datetime_from_format_time.hour,
                    minute=datetime_from_format_time.minute,
                )
                if time_adjusted >= time_now:
                    return_datetime = datetime(
                        year=time_adjusted.year,
                        month=time_adjusted.month,
                        day=time_adjusted.day,
                        hour=time.hour,
                        minute=time.minute,
                    )
                    return return_datetime
                raise ValueError
            except ValueError:
                print("Time must to be equal or greater than current time !")
                continue

    def date_not_less_than_now(self, string: str) -> datetime:
        while True:
            try:
                date = self.input_only_date(string)
                format_date = "%Y-%m-%d"
                datetime_now_formatted = datetime.now().strftime(format_date)
                datetime_from_formatted_date_now = datetime.strptime(
                    datetime_now_formatted, format_date
                ).replace(hour=0, minute=0, second=0)
                if date >= datetime_from_formatted_date_now:
                    return date
                raise ValueError
            except ValueError:
                print("Date must to be equal or greater than current date !")
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
