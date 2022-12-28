import view as v
import models as m


def main_menu_handler():
    while True:
        cmd = v.show_main_menu()
        match cmd:
            case '1':
                return 1
            case '2':
                m.save_as_csv()
                v.send_msg('Сохранение прошло успешно!')
                return 0
            case '0':
                exit(0)
            case _:
                v.send_msg('Такой команды нет :(')


def peoples_list_menu_handler():
    while True:
        v.show_peoples(m.get_peoples())
        cmd = v.show_peoples_list_menu()
        match cmd:
            case '1':
                num = int(v.answer_number_people('просмотра или 0 для отмены'))
                people = m.get_people_by_num(num)
                return 2, people
            case '2':
                first_name = v.answer_people_f_name()
                last_name = v.answer_people_l_name()

                if last_name == '0' or first_name == '0':
                    return 1, None
                m.create_people(first_name, last_name)
                return 1, None
            case '3':
                people_id = m.get_people_by_num(int(v.answer_number_people('изменения')))['id']
                if people_id:
                    first_name = v.answer_people_f_name()
                    last_name = v.answer_people_l_name()

                    if last_name == '0' or first_name == '0':
                        return 1, None
                    m.update_people(people_id, first_name, last_name)
                else:
                    v.send_msg('Вы ввели недопустимое значение')
            case '4':
                people_id = m.get_people_by_num(int(v.answer_number_people('изменения')))['id']
                if people_id:
                    m.delete_people(people_id)
                else:
                    v.send_msg('Вы ввели недопустимое значение')
                return 1, None
            case '0':
                return 0, None
            case _:
                v.send_msg('Такой команды нет :(')


def contacts_menu_handler(people):
    while True:
        v.show_contacts(m.get_phone_numbers(people['id']))
        cmd = v.show_contacts_menu()
        match cmd:
            case '1':
                m.add_phone_number(people['id'],
                                   v.answer_phone_number(),
                                   v.answer_phone_description()
                                   )
                return 2
            case '2':
                m.update_phone_number(people['id'],
                                      v.answer_phone_number(),
                                      v.answer_phone_description()
                                      )
            case '3':
                contact_num = int(v.answer_num_contact_for_delete())
                m.delete_phone_number(people['id'], contact_num)
            case '0':
                return 1
            case _:
                v.send_msg('Такой команды нет :(')
