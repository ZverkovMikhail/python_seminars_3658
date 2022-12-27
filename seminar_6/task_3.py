# 3.	Дан список чисел. Вывести из него только простые числа.
# Ввод	        Вывод
# 15 2 3 31	    2 3 31 33

nums = [15, 2, 3, 31, 19, 8]

for n in nums:
    for i in range(2, int(n / 2)):
        if n % i == 0:
            nums.remove(n)
            break

print(nums)
