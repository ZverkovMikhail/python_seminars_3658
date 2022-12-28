import menu_handler as menu


def main():
    state = 0
    people = None

    while True:
        match state:
            case 0:
                state = menu.main_menu_handler()
            case 1:
                state, people = menu.peoples_list_menu_handler()
            case 2:
                state = menu.contacts_menu_handler(people)
