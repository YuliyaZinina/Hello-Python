print('Введите число, обозначающее день недели')
day_number = int(input())
if 5 < day_number <= 7:
    print('Выходной')
elif day_number > 7:
    print('В неделе 7 дней. Это число не подходит')
else:
    print('Будний')