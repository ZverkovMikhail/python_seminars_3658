# 3.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# o	[1.1, 1.2, 3.1, 5, 10.01] => 0.19


import math

float_nums = [1.1, 1.2, 3.1, 5, 10.01]

remainders_of_float_nums = [round(math.modf(num_f)[0], 2) for num_f in float_nums if isinstance(num_f, float)]

print(max(remainders_of_float_nums) - min(remainders_of_float_nums))
