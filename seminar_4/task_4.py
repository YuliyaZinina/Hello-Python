# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def get_coefficients_list(k):
    coefficients = []

    for i in range(0, k+1):
        coefficients.append(random.choice(range(1, 101)))

    return coefficients


def get_polynomial(coefficients_list):
    k = len(coefficients_list)-1
    text = ''

    for j in range(0, len(coefficients_list)):
        if j == k:
            text += f'{coefficients_list[j]} = 0'
        elif k - j == 1:
            text += f'{coefficients_list[j]}x + '
        else:
            text += f'{coefficients_list[j]}x^{k - j} + '

    return text


k = 4
# print(f'степень k = {k}')

coefficients_list_1 = get_coefficients_list(k)
# print(f'coefficients_list_1 = {coefficients_list_1}')

polynomial_1 = get_polynomial(k, coefficients_list_1)
# print(polynomial_1)

data = open('polynomial.txt', 'w')
data.write(polynomial_1)
data.close()


m = k
# print(f'степень m = {m}')

coefficients_list_2 = get_coefficients_list(m)
# print(f'coefficients_list_2 = {coefficients_list_2}')

polynomial_2 = get_polynomial(m, coefficients_list_2)
# print(polynomial_2)

with open('polynomial_2.txt', 'w') as data_2:
    data_2.write(get_polynomial(m, coefficients_list_2))
