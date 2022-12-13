# 5.	Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).
import random


list = [1, 2, 3, 4, 5, 6]
print(list)

for i in range(len(list)):

    first_el = random.randint(0, len(list)-1)
    second_el = random.randint(0, len(list)-1)

    list[first_el], list[second_el] = list[second_el], list[first_el]

print(list)

