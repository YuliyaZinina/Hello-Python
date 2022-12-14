# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел.
# Ввод чисел продолжается до ввода пустой строки.
# Вход: 36, 12, 144, 18
# Выход: 6

import math


numbers = []
num = 1

while num != '':
    num = input('Введите число: ')
    if num != '':
        numbers.append(int(num))
print(numbers)


gcd = numbers[0]
for i in range(1, len(numbers)):
    gcd = math.gcd(numbers[i], gcd)

print(gcd)
