import random

"""
function to create gameboard
"""


def create_board():
    return [['-' for _ in range(5)] for _ in range(5)]


"""
function to print gameboard
"""


def print_board(board, hide_battleships=False):
    for row in board:
        if hide_battleships:
            print(' '.join(['-' if cell == '1' else cell for cell in row]))
        else:
            print(' '.join(row))


"""
function to place random ships on board
"""


def place_battleships(board):
    battleships_placed = 0
    while battleships_placed < 4:
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if board[x][y] == '-':
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
function to check valid coordinate
"""


def get_valid_coordinate(prompt):
    while True:
        try:
            coordinate = int(input(prompt))
            if coordinate < 0 or coordinate > 4:
                print("Input invalid, please choose a number between 0 and 4")
            else:
                return coordinate
        except ValueError:
            print("Input invalid, please choose a number between 0 and 4")


"""
function to play game
"""


def play_game():
    player_board = create_board()
    place_battleships(player_board)
    computer_board = create_board()
    place_battleships(computer_board)

    print("Its time to play Battleships!!!")
    print("")
    print("The Board is made of coordinates from 0-4 for rows and columns")
    print("Row 0 and column 0 will be the top left of the board")
    print("and row 4 column 4 would be the bottom right")
    print("Try to find where computers battleships are hiding")
    print("Good Luck!")
    print("")
    print("Player Board:")
    print_board(player_board)
    print("")
    print("Computer Board:")
    print_board(computer_board, hide_battleships=True)

    while not is_game_over(player_board) and not is_game_over(computer_board):
        """
        Players Turn
        """
        print("")
        print("Players Turn")
        """ guess_row = int(input("Guess row (0-4): "))
        guess_column = int(input("Guess column (0-4): "))"""
        guess_row = get_valid_coordinate("Guess a row (0-4): ")
        guess_column = get_valid_coordinate("Guess a column (0-4): ")

        if computer_board[guess_row][guess_column] == '1':
            print("")
            print("Well done! You Just sunk a Battleship!")
            computer_board[guess_row][guess_column] = 'X'
        else:
            print("")
            print("Sorry, you have missed")
            computer_board[guess_row][guess_column] = 'M'

        if is_game_over(computer_board):
            break
        """
        Computers Turn
        """
        print("")
        print("Computers Turn")
        computer_guess_row = random.randint(0, 4)
        computer_guess_column = random.randint(0, 4)

        if player_board[computer_guess_row][computer_guess_column] == '1':
            print("")
            print("The Computer has sunk your Battleship")
            player_board[computer_guess_row][computer_guess_column] = 'X'
        else:
            print("")
            print("The Computer has missed")
            player_board[computer_guess_row][computer_guess_column] = 'M'

        print("")
        print("Players Board:")
        print("")
        print_board(player_board)
        print("")
        print("Computers Board:")
        print("")
        print_board(computer_board, hide_battleships=True)

    print("Game Over")
    print("")
    print("Players Board:")
    print("")
    print_board(player_board)
    print("")
    print("Computers Board:")
    print("")
    print_board(computer_board)

    if is_game_over(computer_board):
        print("")
        print("You win the game!")
    else:
        print("")
        print("The Computer won the game")


play_game()
