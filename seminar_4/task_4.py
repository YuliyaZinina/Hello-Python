# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = 2


def get_polynomial(k):
    coefficients = []
    text = ''

    for i in range(0, k+1):
        coefficients.append(random.choice(range(0, 101)))

    print(k)
    print(coefficients)

    for j in range(0, len(coefficients)):
        if j == k:
            text += f'{coefficients[j]} = 0'
        elif k - j == 1:
            text += f'{coefficients[j]}x + '
        else:
            text += f'{coefficients[j]}x^{k - j} + '

    return text


polynomial = get_polynomial(k)
print(polynomial)

data = open('polynomial.txt', 'w')
data.write(polynomial)
data.close()

m = k
with open('polynomial_2.txt', 'w') as data_2:
    data_2.write(get_polynomial(m))