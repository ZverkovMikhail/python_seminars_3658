# 4.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# o	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint


# Возвращает символ степени числа в кодировке utf-8
def get_pow_char_code(n):
    unicode_chars = {
        "0": "\u2070",
        "1": "\u00B9",
        "2": "\u00B2",
        "3": "\u00B3",
        "4": "\u2074",
        "5": "\u2075",
        "6": "\u2076",
        "7": "\u2077",
        "8": "\u2078",
        "9": "\u2079",
    }
    return "".join([unicode_chars[c] for c in str(n)])


# Создает набор коэффициентов заданной длинны
def generate_coefficients(length):
    return [randint(1, 100) for i in range(length)]


# создает многочлен
def create_polynomial(coefficients):
    poly = ''

    for i in reversed(range(len(coefficients))):

        if i > 1:
            poly += f'{coefficients[len(coefficients) -1 - i]}x{get_pow_char_code(i)} + '
        elif i == 1:
            poly += f'{coefficients[len(coefficients) -1 - i]}x + '
        else:
            poly += f'{coefficients[len(coefficients) -1 - i]} = 0'

    print(f'result -> {poly}')
    return poly


# сохраняет строку в файл
def save_to_file(file_name, s):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(s)


k = int(input('Введите натуральную степень k: '))

coeffs1 = generate_coefficients(k + 1)
coeffs2 = generate_coefficients(k + 1)

print(f'coeffs1 -> {coeffs1}')
save_to_file('polynomial1.txt', create_polynomial(coeffs1))

print(f'coeffs2 -> {coeffs2}')
save_to_file('polynomial2.txt', create_polynomial(coeffs2))
