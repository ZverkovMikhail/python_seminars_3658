import view as v
import models as m


def main():
    entries = m.get_data()
    v.show_entries(entries)
    while True:
        cmd = v.show_menu()
        match cmd:
            case '1':
                first_name, last_name, phone = v.request_entry()
                entries['phones'].append({'first_name': first_name, 'last_name': last_name, 'phone': phone})
                m.save_data(entries)
            case '2':
                v.send_msg('Сохранение прошло успешно!' if m.save_as_csv(entries) else 'При сохранении произошла ошибки')
            case '0':
                exit(0)
            case _:
                v.send_msg('Такой команды нет :(')

