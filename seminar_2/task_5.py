# 5.	Удалить вторую цифру трёхзначного числа.

num = 123

print(num // 100, num % 10, sep='')

digits = str(num)
print(digits[0], digits[2], sep='')

