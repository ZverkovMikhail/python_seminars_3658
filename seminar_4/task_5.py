# 5.	Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в
#   словаре различны.
#   Для слова из словаря, записанного в последней строке, определите его синоним.
#   Входные данные	Выходные данные
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye	Bye


def find_synonym(s):

    strs = {'Hello': 'Hi', 'Bye': 'Goodbye', 'List': 'Array'}

    for k, v in strs.items():
        if k.lower() == s.lower():
            return v
        elif v.lower() == s.lower():
            return k
    return 'Не найден!'


print(f'Синоним -> {find_synonym(input("Введите слово: "))}')
