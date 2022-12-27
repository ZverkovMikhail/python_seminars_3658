# 1.	Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел.
# Ввод чисел продолжается до ввода пустой строки.
# Входные данные	    Выходные данные
# 36
# 12
# 144
# 18	                6
import math

# nums = [36,12,144,18]
from functools import reduce


def request_nums():
    nums = []
    while True:
        num = input('Введите натуральное число или пустую строку для завершения ввода: ')
        if not num:
            return nums
        elif not num.isdigit():
            print('Вы ввели некорректное значение!!!')
            continue
        else:
            nums.append(int(num))


def get_gcd_of_list(li):
    # решение в современном python
    # return math.gcd(*li)

    # короткое решение в старых версиях python
    # return reduce(math.gcd, li)

    # решение, которое подразумевалось в задании (как я понял)))
    gsd_temp = min(li)
    for i in range(0, len(li)):
        for j in range(i+1, len(li)):
            g = math.gcd(li[i], li[j])
            if g < gsd_temp:
                gsd_temp = g
    return gsd_temp


print(get_gcd_of_list(request_nums()))
