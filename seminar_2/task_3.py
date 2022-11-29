# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

print('Введите число N')
number = int(input())
summ = 0

for n in range(1, number):
    summ += ((1 + 1 / n) ** n)

print(round(summ, 2))