# 2.	Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет,
# можно ли из этих отрезков составить треугольник.
# Входные данные	     Выходные данные
# triangle(1, 1, 2)	        Это не треугольник
# triangle(7, 6, 10)        Это треугольник

# Сумма двух сторон больше третий


def triangle_check(a, b, c):
    print('Это треугольник' if a + b > c and a + c > b and b + c > a else 'Это не треугольник')


triangle_check(1, 1, 2)
triangle_check(7, 6, 10)
