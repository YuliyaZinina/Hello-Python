# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Допустим, что многочлены полные: в каждом многочлене есть члены с понижающейся степенью переменной и свободный член

import task_4

with open('polynomial.txt', 'r') as data_1:
    polynom_1 = data_1.read()

with open('polynomial_2.txt', 'r') as data_2:
    polynom_2 = data_2.read()


def get_coefficients(polynom):
    list_polynom = polynom[:-4].split(' + ')
    coefficients = list_polynom
    for i in range(0, len(list_polynom)):
        if 'x' in list_polynom[i]:
            ind_x = list_polynom[i].index('x')
            coefficients[i] = list_polynom[i][:ind_x]
    return coefficients


def get_sum_coefficients(list_coefficients_1, list_coefficients_2):
    rev_sum_coefficients = []

    if len(list_coefficients_1) >= len(list_coefficients_2):
        max_len_list = list(reversed(list_coefficients_1))
        min_len_list = list(reversed(list_coefficients_2))
    else:
        max_len_list = list(reversed(list_coefficients_2))
        min_len_list = list(reversed(list_coefficients_1))

    for k in range(0, len(max_len_list)):
        if k < len(min_len_list):
            summa = int(max_len_list[k]) + int(min_len_list[k])
            rev_sum_coefficients.append(summa)
        else:
            rev_sum_coefficients.append(int(max_len_list[k]))

    sum_coefficients = list(reversed(rev_sum_coefficients))
    return sum_coefficients


coefficients_1 = get_coefficients(polynom_1)
coefficients_2 = get_coefficients(polynom_2)

sum_polynom = task_4.get_polynomial(get_sum_coefficients(coefficients_1, coefficients_2))

with open('summ_polynomial.txt', 'w') as data_sum:
    data_sum.write(sum_polynom)
