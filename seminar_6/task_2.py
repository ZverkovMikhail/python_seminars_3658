# 2.	На первой строке вводится натуральное число N — количество строк.
# Далее следуют N строк, которые надо будет отсортировать
# Ввод	Вывод
# 4
# три
# четыре
# пять
# шесть	три
#         пять
#         шесть
#         четыре


lines = ['три',
         'четыре',
         'пять',
         'шесть']

lines.sort(key=len)

for line in lines:
    print(line)

