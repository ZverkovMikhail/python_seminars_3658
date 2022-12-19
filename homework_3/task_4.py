# 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное
# (встроенными методами пользоваться нельзя).
# Пример:
# 	45 -> 101101
# 	3 -> 11
# 	2 -> 10


# преобразовывает десятичное число в двоичное
def dec_to_bin(num):
    bin_str = ''
    while num > 0:
        bin_str += str(num % 2)
        num = num // 2
    return bin_str[::-1]


num1 = 45
num2 = 3
num3 = 2

print(f'{num1} -> {dec_to_bin(num1)}')
print(f'{num2} -> {dec_to_bin(num2)}')
print(f'{num3} -> {dec_to_bin(num3)}')


