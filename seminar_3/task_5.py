# 5.	Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# •	список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# •	список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# •	список: [], ищем: "123", ответ: -1


def second_occurrence_position(elems, find):
    is_first = False
    for i in range(len(elems)):
        if elems[i] is find:
            if is_first:
                return i
            is_first = True
    return -1


def print_result(elems, find):
    print(f'список: {elems} ищем: "{find}" ответ: {second_occurrence_position(elems, find)}')


list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
list4 = ["123", "234", 123, "567"]
list5 = []


print_result(list1, "qwe")
print_result(list2, "йцу")
print_result(list3, "йцу")
print_result(list4, "123")
print_result(list5, "123")