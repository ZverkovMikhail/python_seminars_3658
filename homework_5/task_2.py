# 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint
from time import sleep

candies_count = 0
max_candies = 0
players = []
whose_turn = 0


def is_bot(name):
    return name.lower() == 'bot'


def bot_turn(candies, max_candy):
    if candies <= max_candy or candies == max_candy + 1:
        print(1)
        taken = max_candy

    elif candies < max_candy * 2 + 1:
        print(max_candy * 2 + 1)
        taken = candies - max_candy - 1

    else:
        print(3)
        taken = max_candy

    print(f'Бот взял {taken} конфет')
    return taken


def init():
    global candies_count
    global max_candies
    global players
    global whose_turn

    candies_count = 100
    max_candies = 28

    print('На столе лежит 2021 конфета.\n'
          'Играют два игрока делая ход друг после друга.'
          'Первый ход определяется жеребьёвкой.\n'
          'За один ход можно забрать не более чем 28 конфет.\n'
          'Все конфеты оппонента достаются сделавшему последний ход.\n\n'
          'Для игры против бота одного из игроков назовите Bot\n ')

    players = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]
    # players = ['Misha', 'bot']

    whose_turn = randint(0, len(players) - 1)


init()

while candies_count > 0:
    sleep(1)
    print(f'Осталось {candies_count} Конфет:')

    if max_candies > candies_count:
        max_candies = candies_count

    try:
        if is_bot(players[whose_turn]):
            taken_candies = bot_turn(candies_count, max_candies)
        else:
            taken_candies = int(input(f'{players[whose_turn]} ваш ход!\nВведите количество конфет которое берете: '))

        if 1 > taken_candies or taken_candies > max_candies:
            raise ValueError

    except ValueError:
        print(f'\nСтолько взять нельзя! возьмите от 1 до {max_candies}!!!\n')
        continue

    candies_count -= taken_candies

    if candies_count <= 0:
        result = 'Вы проиграли!(( В другой раз повезет!' \
            if is_bot(players[whose_turn]) else f'!!! {players[whose_turn]}, поздравляю Вы победили !!!'

        answer = input(f'\n{result}\n '
                       f'если хотите сыграть еще введите Y, для выхода любой другой символ: \n')

        if answer.lower() == 'y':
            init()
            continue
        else:
            break
    else:
        whose_turn = not whose_turn
