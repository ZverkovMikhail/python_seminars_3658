# 2.	Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]


# Возвращает произведение пар чисел списка
def prod_of_pairs(nums):
    answer = []
    for i in range(((len(nums) + 1) // 2)):
        answer.append(nums[i] * nums[len(nums) - 1 - i])
    return answer


nums1 = [2, 3, 4, 5, 6]
nums2 = [2, 3, 5, 6]

print(prod_of_pairs(nums1))
print(prod_of_pairs(nums2))

