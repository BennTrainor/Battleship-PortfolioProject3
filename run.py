import random

"""
function to create gameboard
"""
def create_board():
    return [['0' for _ in range(5)] for _ in range(5)]

"""
function to print gameboard
"""
def print_board(board):
    for row in board:
        print(' '.join(row))

board = create_board()
print_board(board)


