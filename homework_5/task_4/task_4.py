# 4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import re


def get_input_data(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def create_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)


def zip_file(file_name, data):
    count = 1
    temp_char = data[0]
    output_data = ''

    for i in range(1, len(data)):

        if data[i] != temp_char:
            output_data += f'{count}{temp_char}'
            count = 1
            temp_char = data[i]
        else:
            count += 1

    output_data += f'{count}{temp_char}'
    create_file(file_name + '.zp', output_data)


def unzip_file(file_name, data):
    output_data = ''
    pairs = re.findall(r'(\d+)(.)', data)
    for count, char in pairs:
        output_data += char * int(count)
    create_file(file_name, output_data)


file_n = 'input_data'

zip_file('input_data', get_input_data(file_n))
unzip_file('output_data', get_input_data(file_n + '.zp'))
