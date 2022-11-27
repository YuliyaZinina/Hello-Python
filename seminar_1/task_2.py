# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            a = not (x or y or z)
            b = (not x) and (not y) and (not z)
            c = a == b

            # print(x, y, z)
            # print(c)

if c == True:
    print('Выражение истинно')
else:
    print('Выражение ложно')