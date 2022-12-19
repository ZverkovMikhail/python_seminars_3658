# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib(n):
    if n in {0, 1}:
        return n
    return fib(n - 1) + fib(n - 2)


fibs = []
for i in range(-8, 9):
    if i < 0:
        fibs.append(int((-1) ** (i + 1) * fib(abs(i))))
    else:
        fibs.append(fib(i))
print(fibs)
