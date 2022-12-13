#5.	Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве.

import math


# Запрос значений у пользователя
def request_coordinates():
    while True:

        coordinates = input('Введите координаты точек x1, y1, x2, y2 через запятую: ').split(',')

        try:
            x1 = int(coordinates[0])
            y1 = int(coordinates[1])
            x2 = int(coordinates[2])
            y2 = int(coordinates[3])
        except ValueError:
            print('вы ввели не числовое значение, попробуйте еще раз')
            continue

        return x1, y1, x2, y2


# Определение расстояния между точками
def find_distance(coords):
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


points_coord = request_coordinates()

print(f'A ({points_coord[0]},{points_coord[1]}); B ({points_coord[2]},{points_coord[3]}) -> '
      f'{round(find_distance(points_coord), 3)}')
