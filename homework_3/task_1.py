# 1.	Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на
# нечётной позиции.
# Пример:
# o	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# nums = [2, 3, 5, 9, 3]


# Запрос списка чисел у пользователя
def request_list():
    nums = []

    while True:
        data = input('Введите число или "end" для завершения: ')
        if data.lower() == 'end':
            break
        elif data.isnumeric():
            nums.append(int(data))
        else:
            print('вы ввели не корректное значение!')
            continue
    return nums


print('ответ: {}'.format(sum(request_list()[1::2])))
