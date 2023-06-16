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


"""
function to place random ships on board
"""


def place_battleships(board):
    battleships_placed = 0
    while battleships_placed < 4:
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if board[x][y] == '0':
            board[x][y] = '1'
            battleships_placed += 1

"""
function to check if game is over
"""

def is_game_over(board):
    for row in board:
        if '1' in row:
            return False
        return True

"""
function to play game
"""

def play_game():
    board = create_board()
    place_battleships(board)
    print("Its time to play Battleships!!!")
    print_board(board)
