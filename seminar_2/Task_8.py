# 2.	Определите среднее значение всех элементов последовательности, завершающейся числом 0.

# num = None
# sum = 0
# count = 0
# while True:
#     num = int(input('Введите число: '))
#     if num == 0:
#         break
#
#     sum += num
#     count += 1
#
#
# if count > 0:
#     print(round(sum / count, 2))


nums = []
while True:
    num = int(input('Введите число: '))
    if num != 0:
        nums.append(num)
    else:
        break

if len(nums) > 0:
    print(round(sum(nums)/len(nums), 2))
