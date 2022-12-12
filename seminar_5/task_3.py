# Создайте программу для игры в "Крестики-нолики".

# Создайте программу для игры в "Крестики-нолики".

import random

moves = 9
field = [i for i in range(1, 10)]
print(field[0:3], '\n', field[3:6], '\n', field[6:9])

print('Начнем игру')
players_list = [input(f'Введите имя игрока {i + 1}: ') for i in range(0, 2)]

first_player_name = players_list[0]
second_player_name = players_list[1]

# Кто ходит ноликами?
player_name = random.choice(players_list)

# Определяем первый ход
print(f'Первый ход делает {player_name}')
symbol = 'O'

# Ход
while moves > 0:

    position = input(f'{player_name}, куда поставишь {symbol}? Введи номер позиции: ')

    # Проверяем не занята ли клетка и занимаем, если свободна
    while field[int(position) - 1] == 'O' or field[int(position) - 1] == 'X':
        print('Надо выбрать другую позицию')
        position = input(f'{player_name}, куда поставишь {symbol}? Введи номер позиции: ')
    else:
        field[int(position) - 1] = symbol

    print(field[0:3], '\n', field[3:6], '\n', field[6:9])

    # Проверяем выигрыш
    if field[0] == field[1] == field[2] or \
            field[3] == field[4] == field[5] or \
            field[6] == field[7] == field[8] or \
            field[0] == field[4] == field[8] or \
            field[2] == field[4] == field[6] or \
            field[0] == field[3] == field[6] or \
            field[1] == field[4] == field[7] or \
            field[2] == field[5] == field[8]:
        moves = 0
        print(f'{player_name} выиграл!')
    else:
        moves -= 1

    # Меняем игрока и символ
    if moves != 0:
        if player_name == first_player_name:
            player_name = second_player_name
        else:
            player_name = first_player_name

        if symbol == 'O':
            symbol = 'X'
        else:
            symbol = 'O'

