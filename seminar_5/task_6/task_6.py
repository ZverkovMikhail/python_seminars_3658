# Предположим, вы переписываете у друга рецепты в блокнотик, но вам не нравится лук. Переписывайте без него.
# Формат ввода
# На первой строке вводится натуральное число N — количество пунктов рецепта.
# Далее следуют N строк — пункты рецепта.
#
# Формат вывода
# Одна строка — пункты рецепта, разделённые запятой и пробелом, без пунктов с упоминанием лука
# (то есть таких, в которых нет подстроки "лук" в нижнем регистре).
# ввод

data = []
count = 0
with open('recept.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines.pop(0)
    data = list(map(lambda l: l.replace('\n', ''), filter(lambda l: 'лук' not in l.lower(), lines)))

# print(list(data))
# print(count)

with open('recept_without_onion.txt', 'w', encoding='utf-8') as f:
    f.write(', '.join(data))
