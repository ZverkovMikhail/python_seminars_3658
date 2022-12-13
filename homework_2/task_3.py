#3. Задайте список из n чисел последовательности(1 + 1 / n) ^ n выведите на экран их сумму.


n = int(input('Введите число N: '))

nums = []
for i in range(1, n+1):
    nums.append((1 + 1 / i) ** i)

print(round(sum(nums), 2))

