# 2.	Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            print(f'x={x} y={y} z={z} -> {not(x or y or z) == ((not x) and (not y) and (not z))}')

