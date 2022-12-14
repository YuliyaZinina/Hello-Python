# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ),
# применив лямбды, filter, map, zip, enumerate, списочные выражения.

# LIST COMPREHENSION
# Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

number = 4

list = [i for i in range(-number, number + 1)]
print(list)

with open("file.txt", "r") as data:
    result = list[int(data.read(1))] * list[int(data.read(2))]

print(result)
