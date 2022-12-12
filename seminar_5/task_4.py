# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

with open('task_4_input.txt', 'w') as input_data:
    input_data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('task_4_input.txt', 'r') as input_data:
    input_text = input_data.read()

print(input_text)


def get_compressed_text(text):
    compressed = ''
    count = 1
    for i in range(1, len(text)):

        if text[i] == text[i - 1]:
            count += 1

        else:
            compressed += str(count)
            compressed += text[i - 1]

            count = 1

    compressed += str(count)
    compressed += text[i]
    return compressed


def get_decompressed_text(compressed):
    count_list = []
    letter_list = []
    count = ''

    for i in range(0, len(compressed)):
        if compressed[i].isdigit():
            count += compressed[i]
            if compressed[i + 1].isalpha():
                letter_list.append(compressed[i + 1])
                count_list.append(count)
                count = ''

    decompressed = ''
    for k in range(0, len(count_list)):
        for j in range(0, int(count_list[k])):
            decompressed += letter_list[k]
    return decompressed


compressed_text = get_compressed_text(input_text)
print(compressed_text)

with open('task_4_output.txt', 'w') as output_data:
    output_data.write(compressed_text)

decompressed_text = get_decompressed_text(compressed_text)
print(decompressed_text)

with open('task_4_decompressed.txt', 'w') as output_data:
    output_data.write(decompressed_text)
