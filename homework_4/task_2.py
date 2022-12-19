# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input('Введите число N: '))
factors = []

for i in range(2, n + 1):
    if n % i == 0:
        factors.append(i)
        n = n / i
        i = 2

    if i >= n:
        break

print(factors)
