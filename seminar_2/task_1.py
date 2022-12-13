# 1.	Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел:
# 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

nums = [5, 10, 5]

max_count = 1
for i in range(len(nums) - 1):
    count = nums.count(nums[i])
    if count > max_count:
        max_count = count
print(max_count)
