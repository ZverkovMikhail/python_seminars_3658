# 3.	Создайте программу для игры в "Крестики-нолики".
import os
import random
from random import randint
from time import sleep


SYMBOLS = ['0', 'X']


def print_field(board):
    count = 0
    print('\n')
    for el in board:
        if count == 3:
            print('')
            count = 0
        print(f'{el} ', end='')
        count += 1
    print('')


def turn(board, pos, whose_turn):
    symbol = SYMBOLS[whose_turn]
    for el in board:
        if pos in el:
            board[board.index(pos)] = symbol
            return board
    return None


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def start():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    whose_turn = True
    while True:

        print('Ходит игрок играющий за {}'.format(SYMBOLS[whose_turn]))
        print_field(board)
        pos = input('Введите номер секции на которую хотите походить: ')
        if not pos.isdigit() or 1 > int(pos) > 9:
            print('!!! Данная позиция не доступна !!!')
            continue
        board = turn(board, pos, whose_turn)

        winner = check_win(board)
        if winner:
            print(f'победил -> {check_win(board)} \n!!! С чем его и поздравляем!!!)')
            break

        whose_turn = not whose_turn


start()

