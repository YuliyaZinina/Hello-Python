# Задайте числами список из N элементов, заполненных из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

number = 4

list = []

for i in range(-number, number+1):
    list.append(i)

print(list)

with open("file.txt", "r") as data:
    pos1 = int(data.read(1))
    pos2 = int(data.read(2))
    # print(pos1, pos2)
    
result = list[pos1] * list[pos2]

print(list[pos1], list[pos2], result)
    