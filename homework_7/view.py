def show_menu():
    print('\nМеню:\n'
          '1 - добавить запись \n'
          '2 - сохранить в csv \n'
          '0 - выход из программы\n')
    return input('Введите команду: ')


def show_entries(entries):
    print('\n')
    if entries['phones']:
        for entry in entries['phones']:
            print('{} {} -> {}'
                  .format(entry['first_name'], entry['last_name'], entry['phone'])
                  )
    else:
        print('Записей нет!')


def request_entry():
    first_name = input('Введите имя: ')
    last_name = input('Введите Фамилию: ')
    phone = input('Введите телефон: ')
    return first_name, last_name, phone


def send_msg(text):
    print(f'-->> {text} \n')
