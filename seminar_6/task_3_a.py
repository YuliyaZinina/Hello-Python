
# LAMBDA
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]


with open('task_1_text.txt', 'r') as data:
    text = data.read()

new_list = list(filter(lambda x: ('абв' not in x), text.split()))

with open('task_1_new_text.txt', 'w') as new_data:
    for i in new_list:
        new_data.write(i + ' ')
