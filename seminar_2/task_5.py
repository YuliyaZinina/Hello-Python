# Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно).

import random
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(a)-1, 1, -1):
    n = random.choice(range(0, i))
    a[n], a[i] = a[i], a[n]

print(a)
