# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# (встроенными методами пользоваться нельзя).
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

print('Введите число')
number = int(input())
binary_list = []

while number > 0:
    r = number // 2
    q = number % 2
    number = r
    binary_list.insert(0, q)
print(binary_list)