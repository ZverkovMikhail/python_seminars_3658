import json
import os
import sqlite3 as db


def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d


conn = db.connect('phones.sqlite')
conn.execute("PRAGMA foreign_keys = 1")
conn.row_factory = dict_factory
cursor = conn.cursor()


def get_peoples():
    cursor.execute("select * from peoples")
    results = cursor.fetchall()
    return results


def get_people(people_id):
    cursor.execute(f"select * from peoples WHERE id={people_id}")
    results = cursor.fetchone()
    return results


def get_people_by_num(num):
    try:
        peoples = get_peoples()
        people_id = peoples[num - 1]['id']
        cursor.execute(f"select * from peoples WHERE id={people_id}")
        results = cursor.fetchone()
    except Exception:
        return None
    return results


def get_people_by_number(number_id):
    return get_people(get_phone_number(number_id)['people'])


def create_people(first_name, last_name=''):
    cursor.execute(
        f"INSERT INTO peoples (f_name, l_name) VALUES ('{first_name}','{last_name}')")
    conn.commit()
    return get_peoples()


def update_people(people_id, first_name='', last_name=''):
    original_entry = get_people(people_id)

    if not first_name:
        f_name = original_entry['f_name']
    else:
        f_name = first_name

    if not last_name:
        l_name = original_entry['l_name']
    else:
        l_name = last_name

    cursor.execute(
        f"UPDATE peoples SET f_name='{f_name}', l_name='{l_name}' WHERE id='{people_id}'")
    conn.commit()
    return get_peoples()


def delete_people(people_id):
    cursor.execute(f"DELETE FROM peoples WHERE id='{people_id}'")
    conn.commit()
    return get_peoples()


def get_phone_numbers(people_id):
    cursor.execute(f"select id, number, description from phone_numbers WHERE people='{people_id}'")
    results = cursor.fetchall()
    return results


def get_phone_numbers_by_people_num(num):
    try:
        peoples = get_peoples()
        people_id = peoples[num - 1]['id']
        cursor.execute(f"select id, people, number, description from phone_numbers WHERE people='{people_id}'")
        results = cursor.fetchall()
    except Exception:
        return None
    return results


def get_phone_number(number_id):
    cursor.execute(f"select id, people, number, description from phone_numbers WHERE id='{number_id}'")
    results = cursor.fetchone()
    return results


def add_phone_number(people_id, number, description):
    cursor.execute(f"INSERT INTO phone_numbers(people, number, description) "
                   f"VALUES ('{people_id}','{number}','{description}')")
    conn.commit()


def update_phone_number(number_id, number='', description=''):
    original_entry = get_phone_number(number_id)

    if not number:
        num = original_entry['number']
    else:
        num = number

    if not description:
        desc = original_entry['description']
    else:
        desc = description

    cursor.execute(
        f"UPDATE phone_numbers SET number='{num}', description='{desc}' WHERE id='{number_id}'")

    conn.commit()
    return get_phone_numbers(original_entry['people'])


def delete_phone_number(people_id, num):
    numbers = get_phone_numbers(people_id)
    number_id = numbers[num - 1]['id']
    cursor.execute(f"DELETE FROM phone_numbers WHERE id='{number_id}'")
    conn.commit()


def save_as_csv():
    peoples = get_peoples()
    with open('phones.csv', 'w') as pf:
        for people in peoples:
            pf.write('{} {}\n'
                     .format(people['f_name'], people['l_name'])
                     )
            for contact in get_phone_numbers(people['id']):
                pf.write('{};{}\n'
                         .format(contact['description'], contact['number'])
                         )
