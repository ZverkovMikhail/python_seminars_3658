# 1.	Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 	6782 -> 23
# 	0.56 -> 11


# Запрашиваем вещественное число
def request_float():
    return float(input('Введите вещественное число: '))


# находим сумму цифр вещественного числа
def sum_of_digits(num):
    digits = list(str(num))
    digits.remove('.')
    return sum([int(x) for x in digits])


print(sum_of_digits(request_float()))

