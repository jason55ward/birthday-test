#!/usr/bin/env python3
import pytest
import datetime
from birthday import get_birthday_list
from faker import Faker
fake = Faker.fake()


def generate_example_data(rows=4, specific_date=''):
    data = []
    for row in range(rows):
        first_name = fake.first_name()
        last_name = fake.last_name()
        date = specific_date if specific_date else fake.date()
        data.append([last_name, first_name, date])
    return data

def test_generate_example_data():
    rows = 10
    data = generate_example_data(rows=rows)
    assert len(data) == rows

def test_leap_year_birthdays():
    data = generate_example_data(rows=10,specific_date='1756/02/29')
    birthdays = get_birthday_list(data, custom_today_date='1760/02/29')
    assert len(birthdays) == len(data)

def test_non_leap_year_birthdays():
    data = generate_example_data(rows=10,specific_date='1456/02/29')
    birthdays = get_birthday_list(data, custom_today_date='1475/02/28')
    assert len(birthdays) == len(data)

def test_dateformat_long():
    data = generate_example_data(rows=1,specific_date='12 Jun, 2018')
    birthdays = get_birthday_list(data, custom_today_date='2020/6/12')
    assert len(birthdays) == len(data)

def test_dateformat_other():
    data = generate_example_data(rows=1,specific_date='9-5-1988')
    birthdays = get_birthday_list(data, custom_today_date='1988/9/5')
    assert len(birthdays) == len(data)
