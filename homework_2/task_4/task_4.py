# 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from pathlib import Path


n = int(input('Введите число N: '))

nums = list(range(-n, n + 1))

print(nums)

with open(Path(__file__).parent.resolve() / 'file.txt', 'r') as file:

    mult = 1

    for num in file:
        mult *= nums[int(num)]

    print(mult)
