# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def get_coordinates():
    coordinates = []
    for i in range(2):
        print(f'Введите координату {i + 1}')
        coordinates.append(int(input()))
        i += 1
    return coordinates

print('Введите координаты точки А')
coordinates_a = get_coordinates()

print('Введите координаты точки B')
coordinates_b = get_coordinates()

print(f'A {coordinates_a}')
print(f'B {coordinates_b}')

distance = round(((((coordinates_b[0] - coordinates_a[0]) ** 2) + ((coordinates_b[1] - coordinates_a[1]) ** 2)) ** 0.5), 2)

print(f' Расстояние между точками А и В = {distance}')
