# 3.	Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# Подсказка: можно использовать модуль datetime

from datetime import datetime as dt
import math, time


def my_rand(start, end):
    ts = dt.timestamp(dt.now())
    return int(abs(math.sin(ts) * (end - start) + start))


def my_rand2(start, end):
    rand = math.modf(time.time())[0]
    return int(rand * (end - start) + start)


print(my_rand(0, 10))
print(my_rand2(0, 10))
