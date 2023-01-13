# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


import random

candies = 100
candies_to_get = 28

print('Начнем игру с Ботом')
players_list = ['Bot']

players_list.append(input('Введите ваше имя: '))

# Кто ходит первым?
player_name = random.choice(players_list)
print(f'Первый ход делает {player_name}')

while candies > 0:
    if candies < 28:
        candies_to_get = candies
    else:
        candies_to_get = 28
    # ход
    if player_name == players_list[0]:
        turn = candies % (candies_to_get + 1)
        print(f'Бот ходит и забирает {turn} конфет')
        candies -= turn
        print(f'Осталось {candies} конфет')
    else:

        print(f'{players_list[1]}, твой ход! Можно взять не больше {candies_to_get} конфет. Сколько конфет берёшь?')
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
        if player_name == players_list[0]:
            player_name = players_list[1]
        else:
            player_name = players_list[0]

else:
    print(f'Конфет не осталось! Выиграл {player_name}!')