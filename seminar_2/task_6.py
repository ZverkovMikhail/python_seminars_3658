# 6.	Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество
# вхождений одной строки в другой.

# first_str = input('Введите стороку: ')
# second_str = input('Введите вторую стороку: ')

first_str = 'maaabmaamaaa'
second_str = 'aa'

i = 0
count = 0

while i < len(first_str):
    if first_str[i:i + len(second_str)] == second_str:
        count += 1
        i += (len(second_str) - 1)
    else:
        i += 1

print(count)

