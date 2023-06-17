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
    player_board = create_board()
    place_battleships(player_board)
    computer_board = create_board()
    place_battleships(computer_board)

    print("Its time to play Battleships!!!")
    print("Player Board")
    print_board(player_board)

    while not is_game_over(player_board) and not is_game_over(computer_board):
        """
        Players Turn
        """
        print("Players Turn")
        guess_row = int(input("Guess row (0-4): "))
        guess_column = int(input("Guess column (0-4): "))

        if computer_board[guess_row][guess_column] == '1':
            print("Well done! You Just sunk a Battleship!")
            computer_board[guess_row][guess_column] = 'X'
            player_board[guess_row][guess_column] = 'X'
        else:
            print("Sorry, you have missed")
            player_board[guess_row][guess_column] = 'M'

        print("Player Board")
        print_board(player_board)

        if is_game_over(computer_board):
            break
        """
        Computers Turn
        """
        print("Computers Turn")
        computer_guess_row = random.randint(0, 4)
        computer_guess_column = random.randint(0, 4)

        if player_board[computer_guess_row][computer_guess_column] == '1':
            print("The Computer has sunk your Battleship")
            player_board[computer_guess_row][computer_guess_column] = 'X'
            computer_board[computer_guess_row][computer_guess_column] = 'X'
        else:
            print("The Computer has missed")
            computer_board[computer_guess_row][computer_guess_column] = 'M'

        print("Players Board:")
        print_board(player_board)

    print("Game Over")
    print_board(player_board)

    if is_game_over(player_board):
        print("You win the game!")
    else:
        print("The Computer won the game")


play_game()
