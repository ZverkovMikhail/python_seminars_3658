# 5.	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.
import re


# Считывает многочлен из файла
def get_poly(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readline()


# Извлекает коэффициенты из многочлена
def parse_coeffs(poly):
    return re.findall(r'(\d+)', poly.split('=')[0])


# Суммирует коэффициенты любого количества многочленов любой длинны
def sum_of_poly_coeffs(*args):
    coeffs_max_length = max(args, key=len)

    result = [0 for i in range(len(coeffs_max_length))]

    for i in range(len(coeffs_max_length)):
        for j in range(len(args)):
            if len(args[j]) - 1 - i >= 0:
                result[len(result) - 1 - i] += int(args[j][len(args[j]) - 1 - i])
    return result


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


coeffs1 = parse_coeffs(get_poly('polynomial1.txt'))
coeffs2 = parse_coeffs(get_poly('polynomial2.txt'))

print(f'coeffs1 = {coeffs1}')
print(f'coeffs2 = {coeffs2}')
save_to_file('polynomial_result.txt', create_polynomial(sum_of_poly_coeffs(coeffs1, coeffs2)))
