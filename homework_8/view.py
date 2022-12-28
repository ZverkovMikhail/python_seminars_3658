def show_main_menu():
    print('\nМеню:\n'
          '1 - Список людей \n'
          '2 - импорт в csv \n'
          '0 - выход из программы\n')
    return input('Введите команду: ')


def show_peoples_list_menu():
    print('\nМеню:\n'
          '1 - Посмотреть контакты человека\n'
          '2 - Добавить нового человека\n'
          '3 - изменить человека\n'
          '4 - удалить человека\n'
          '0 - назад\n')
    return input('Введите команду: ')


def show_contacts_menu():
    print('\nМеню:\n'
          '1 - Добавить новый контакт\n'
          '2 - изменить контакт\n'
          '3 - удалить контакт\n'
          '0 - назад\n')
    return input('Введите номер контакта: ')


def show_peoples(entries):
    print('\n')

    if entries:
        for idx, entry in enumerate(entries, 1):
            print(f"{idx} - {entry['l_name']} {entry['f_name']}")
    else:
        print('Записей нет!')
    return entries


def show_contacts(entries):
    print('\n')

    if entries:
        for idx, entry in enumerate(entries, 1):
            print(f"{idx} - {entry['number']} {entry['description']}")
    else:
        print('контактов пока нет нет!')


def add_people():
    first_name = input('Введите имя: ')
    last_name = input('Введите Фамилию: ')
    return first_name, last_name


def answer_number_people(cause_prompt):
    return input(f'Введите номер записи для {cause_prompt}: ')


def answer_people_f_name():
    return input(f'Введите имя: ')


def answer_people_l_name():
    return input(f'Введите фамилию: ')


def answer_num_contact_for_delete():
    return input(f'Введите номер контакта для удаления: ')


def answer_phone_number():
    return input(f'Введите номер телефона: ')


def answer_phone_description():
    return input(f'Введите описание: ')


def send_msg(text):
    print(f'-->> {text} \n')
