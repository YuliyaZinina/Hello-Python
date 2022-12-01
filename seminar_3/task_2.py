# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6, 7, 2]
new_list = []
middle = len(list) // 2 + len(list) % 2

for i in range(0, middle):
    print(i)
    n = len(list)-1-i
    print(n)
    new_list.append(list[i]*list[n])
print(new_list)
