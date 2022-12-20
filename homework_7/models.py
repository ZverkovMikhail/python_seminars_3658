import json
import os


def get_data():
    if os.path.exists('phones.json'):
        with open('phones.json', 'r', encoding='utf-8') as pf:
            return json.loads(pf.read())
    return {'phones': []}


def save_data(entries):
    with open('phones.json', 'w', encoding='utf-8') as pf:
        pf.write(json.dumps(entries))


def save_as_csv(entries):
    with open('phones.csv', 'w', encoding='utf-8') as pf:
        if entries['phones']:
            for entry in entries['phones']:
                pf.write('{};{};{}\n'
                         .format(entry['first_name'], entry['last_name'], entry['phone'])
                         )
            return True
    return False
