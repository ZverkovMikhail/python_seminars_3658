# 2.	Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# Входные данные	Выходные данные
# 1 5 2 4 3	        5
#                   4

nums = [1, 5, 2, 4, 3]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        print(nums[i])
