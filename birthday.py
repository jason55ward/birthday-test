import json
import os

EXAMPLE_JSON_FILE='example.json'
DEFAULT_JSON=[
	["Doe", "John", "1982/10/08"],
	["Wayne", "Bruce", "1965/01/30"],
	["Gaga", "Lady", "1986/03/28"],
	["Mark", "Curry", "1988/02/29"]
]


def get_birthday_list(data, custom_today_date=None):
    result = []
    for row in data:
        pass
    return result

def get_data(filename=None):
    if filename and os.path.exists(os.path.join('./',filename)):
        data=[]
    else:
        print(f'File {filename} not found. Using {EXAMPLE_JSON_FILE} instead.')
        if not os.path.exists(os.path.join('./',EXAMPLE_JSON_FILE)):
            pass #write file from DEFAULT_JSON
    return data


if __name__ == "__main__":
    data = get_data()
    birthday_list = get_birthday_list(data)
    if birthday_list:
        print(birthday_list)
    else:
        print('There are no birthdays today')
