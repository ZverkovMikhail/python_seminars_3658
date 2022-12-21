# 1.	В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы
# выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Входные данные	Выходные данные
# 1 2 3 5 6 7 8 	4


nums = []

with open('nums.txt', 'r') as f:
    nums = f.read().split(' ')

nums = list(map(int, nums))

count = 0
for i in range(1, len(nums)):
    if nums[i] - 1 != nums[i-1]:
        print(nums[i] - 1)

