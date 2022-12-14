# 2.	Орел и решка
#
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла,
# а буква "Р" – соответствует выпадению Решки. Напишите программу,
# которая подсчитывает наибольшее количество подряд выпавших Решек.
#
# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
#
# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.
#
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
# Входные данные	                                            Выходные данные
# ОРРОРОРООРРРО	                                                3
# ООООООРРРОРОРРРРРРР                                           7
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР      31


EAGLE_CHAR = 'Р'

str_1 = 'ОРРОРОРООРРРО'
str_2 = 'ООООООРРРОРОРРРРРРР'
str_3 = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'
str_4 = 'ОООО'


def eagle_count(st):
    counts = []
    count_temp = 0
    is_eagle = False # используется для исключения

    for c in list(st):

        if c == EAGLE_CHAR:
            is_eagle = True
            count_temp += 1
        elif is_eagle:
            is_eagle = False
            counts.append(count_temp)
            count_temp = 0

    if is_eagle:
        counts.append(count_temp)

    if counts:
        return max(counts)
    else:
        return 0


print(eagle_count(str_1))
print(eagle_count(str_2))
print(eagle_count(str_3))
print(eagle_count(str_4))

