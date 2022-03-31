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
        print(row)
    return result

def get_data(filename=None):
    data = []
    if filename and os.path.exists(os.path.join('./',filename)):
        with open(os.path.join('./',filename)) as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError:
                print(f"Invalid JSON in {filename}")
    else:
        if filename:
            print(f'File {filename} not found. Using {EXAMPLE_JSON_FILE} instead.')
        if os.path.exists(os.path.join('./',EXAMPLE_JSON_FILE)):
            with open(os.path.join('./',EXAMPLE_JSON_FILE)) as json_file:
                try:
                    data = json.load(json_file)
                except json.decoder.JSONDecodeError:
                    print(f"Invalid JSON in {EXAMPLE_JSON_FILE}")
        else:
            with open(os.path.join('./',EXAMPLE_JSON_FILE), 'w') as json_file:
                json_file.write(json.dumps(DEFAULT_JSON))
            data=DEFAULT_JSON
    return data


if __name__ == "__main__":
    import argparse
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("--file", "-f", type=str, required=False)
    filename = cli_parser.parse_args().file

    data = get_data(filename)
    if data:
        birthday_list = get_birthday_list(data)
        if birthday_list:
            print(birthday_list)
        else:
            print('There are no birthdays today')
