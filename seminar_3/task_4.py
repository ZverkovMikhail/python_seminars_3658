# 4.	Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# Входные данные	Выходные данные
# 12              да
# Строка1
# Строка2
# Строка3
# Строка45
# Стр12ка


def there_is_number(str_list, num):
    for i in str_list:
        if i.__contains__(str(num)):
            return True
    return False


strings = ['Строка1', 'Строка2', 'Строка3', 'Строка45', 'Стр12ка']
print('Да' if there_is_number(strings, 12) else 'Нет')
print('Да' if any('12' in el for el in strings) else 'Нет')
