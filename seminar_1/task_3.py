# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def get_coordinates():
    print('Введите координату Х')
    coord_x = int(input())

    print('Введите координату Y')
    coord_y = int(input())

    return coord_x, coord_y

coord_x, coord_y = get_coordinates()

while coord_x == 0 and coord_y == 0:
    print('Точка находится в начале координат. Введите координаты снова')
    coord_x, coord_y = get_coordinates()

if coord_x > 0 and coord_y > 0:
    print('четверть 1')
elif coord_x < 0 and coord_y > 0:
    print('четверть 2')
elif coord_x < 0 and coord_y < 0:
    print('четверть 3')
elif coord_x > 0 and coord_y < 0:
    print('четверть 3')

elif coord_x == 0:
    print('ось Х')
elif coord_y == 0:
    print('ось Y')
