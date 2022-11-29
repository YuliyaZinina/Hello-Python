# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

print('Введите вещественное число')
number = input()
summ = 0

for n in number:
    # print(n)
    a = n.isdigit()
    # print(a)
    if a == True:
        summ = summ + int(n)
print(summ)
