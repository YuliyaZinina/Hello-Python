# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

print('Введите число N')
number = int(input())
summ = 0
list = []

for n in range(1, number+1):
    a = (1 + 1 / n) ** n
    list.append(round(a, 2))

print(list)

for i in list:
    summ += i

print(summ)
