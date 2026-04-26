from datetime import datetime, timedelta
from random import randint

from tasks.task1 import get_days_from_today
from tasks.task2 import get_numbers_ticket
from tasks.task3 import normalize_phone_number
from tasks.task4 import get_upcoming_birthdays

date = "2021-05-01"
print(f"Task 1: date {date} is {get_days_from_today(date)} days from today \n")

min, max, quantity = 1, 20, 10
numbers = get_numbers_ticket(min, max, quantity)
print(f"Task 2: get {quantity} random numbers between {min} and {max}: {numbers} \n")

phone = "(067) 123 45-67"
print(
    f"Task 3: normalize phone number `{phone}` -> `{normalize_phone_number(phone)}` \n"
)


today = datetime.now()
month = today.month
day = today.day

users = [
    {"name": "Jim Beam"},
    {"name": "John Doe"},
    {"name": "Jane Smith"},
    {"name": "Jefferson Beam"},
    {"name": "Jeffrey Doe"},
    {"name": "John Sr. Doe"},
    {"name": "John Jr. Doe"},
]


def get_random_birthday(index: int) -> datetime:
    date = datetime(randint(1900, 2012), month, day) + timedelta(days=index)
    return date.strftime("%Y.%m.%d")


for i, user in enumerate(users):
    user.update(birthday=get_random_birthday(i))

print(f"Task 4: get upcoming birthdays: {get_upcoming_birthdays(users)} \n")
