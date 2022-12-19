# 2.	Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#   1.	с помощью математических формул нахождения корней квадратного уравнения
#   2.	с помощью дополнительных библиотек Python


import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))

# a = -1
# b = 2
# c = 3

a, b, c = [int(s) for s in input('Введите a b c через пробел: ').split(' ')]

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
