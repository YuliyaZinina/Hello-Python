# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер координатной четверти (1-4)')
quarter_number = int(input())

while quarter_number > 4:
    print('Такой четверти нет. Введите номер координатной четверти (1-4)')
    quarter_number = int(input())

if quarter_number == 1:
    print('x > 0, y > 0')
elif quarter_number == 2:
    print('x < 0, y > 0')
elif quarter_number == 3:
    print('x < 0, y < 0')
elif quarter_number == 4:
    print('x > 0, y < 0')
