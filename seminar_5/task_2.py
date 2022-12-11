# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

candies = 100
players = 2

print('Начнем игру')
players_list = [input(f'Введите имя игрока {i + 1}: ') for i in range(0, players)]

first_player_name = players_list[0]
second_player_name = players_list[1]

# Кто ходит первым?
player_name = random.choice(players_list)
print(f'Первый ход делает {player_name}')

while candies >= 1:
    if candies < 28:
        candies_to_get = candies
    else:
        candies_to_get = 28
    # ход
    print(f'{player_name}, твой ход! Можно взять не больше {candies_to_get} конфет. Сколько конфет берёшь?')
    turn = int(input())

    # Проверяем правильность хода
    while turn > candies_to_get or turn < 1:
        print(f'Столько взять нельзя. Нужно взять 1 - {candies_to_get} конфет')
        turn = int(input())

    # Засчитываем ход
    candies -= turn
    print(f'Осталось {candies} конфет')

    if candies != 0:
        # Меняем игрока
        if player_name == first_player_name:
            player_name = second_player_name
        else:
            player_name = first_player_name

else:
    print(f'Конфет не осталось! Выиграл {player_name}!')