# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,

print('Введите натуральное число от 1 до 100')
number = int(input())

dividers = []

simple_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

if number in simple_numbers:
    dividers.extend([1, number])
else:
    for i in simple_numbers:
        while number % i == 0:
            dividers.append(i)
            number = number // i
            # print(i, number)

print(dividers)