# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
#    точек в этой четверти (x и y).


# Запрос номера четверти у пользователя
def request_quarter():
    while True:

        try:
            quart = int(input('Введите номер четверти: '))
        except ValueError:
            print('вы ввели не числовое значение, попробуйте еще раз')
            continue

        if 1 < quart > 4:
            print('Значения должно находиться в пределах 1-4, попробуйте еще раз')
            continue
        else:
            return quart


# Определение возможных значений по четверти
def find_coordinate_by_quarter(quart):

    match quart:
        case 1:
            return 'x > 0, y > 0'
        case 2:
            return 'x < 0, y > 0'
        case 3:
            return 'x < 0, y < 0'
        case 4:
            return 'x > 0, y < 0'


quarter = request_quarter()
print(f'Допустимые координаты для четверти {quarter}  -> {find_coordinate_by_quarter(quarter)}')
