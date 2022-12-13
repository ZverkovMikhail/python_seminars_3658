# 3.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
#  x=34; y=-30 -> 4
#  x=2; y=4-> 1
#  x=-34; y=-30 -> 3


# Запрос значений у пользователя
def request_coordinate():
    while True:

        coordinates = input('Введите координаты точки x, y через запятую: ').split(',')

        try:
            x = int(coordinates[0])
            y = int(coordinates[1])
        except ValueError:
            print('вы ввели не числовое значение, попробуйте еще раз')
            continue

        if x == 0 or y == 0:
            print('Значения не дожны быть равными 0, попробуйте еще раз')
            continue
        else:
            return x, y


# Определение принадлежности к четверти
def find_quarter(x, y):

    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4


x, y = request_coordinate()
print(f'x = {x} y = {y} -> {find_quarter(x, y)}')
