# 1.	Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


nums = [int(s) for s in input('Введите числа через пробел: ').split(' ')]
print(f'min -> {min(nums)} max -> {max(nums)}')

