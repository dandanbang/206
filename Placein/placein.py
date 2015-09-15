
# INFO 260
# Place-in assessment

from __future__ import print_function
from random import randint

board = []
battleship = []

def create_boards():
    "create two 5x5 board, one for user and one for internal"
    for x in range(5):
        board.append(["O"] * 5)
        battleship.append(["O"] * 5)

def print_board(board):
    "print the user board"
    for row in board:
        print (" ".join(row))

def print_battleship(battleship):
    "print the battleship location"
    for row in battleship:
        print (" ".join(row))

def decides_direction():
    "randomly decides whether the battleship should be vertical or horizontal. 0 = horizontal, 1 = vertical"
    return randint(0, 1)

def generate_random_row(board):
    "chooses a random row number to be the location of the battleship"
    return randint(0, len(board) - 1)

def generate_random_col(board):
    "chooses a random row number to be the location of the battleship"
    return randint(0, len(board[0]) - 1)

def create_battleship1():
    "this function creates the first 3x1 battleship with 50% chance being horizontal and 50% chance being vertical"
    ship_row = generate_random_row(board)
    ship_col = generate_random_col(board)
    if decides_direction() == 0:
        if ship_col > 2:
            battleship[ship_row][2] = "x"
            battleship[ship_row][3] = "x"
            battleship[ship_row][4] = "x"
        else:
            battleship[ship_row][ship_col] = "x"
            battleship[ship_row][ship_col + 1] = "x"
            battleship[ship_row][ship_col + 2] = "x"
    else:
        if ship_row > 2:
            battleship[2][ship_col] = "x"
            battleship[3][ship_col] = "x"
            battleship[4][ship_col] = "x"
        else:
            battleship[ship_row][ship_col] = "x"
            battleship[ship_row + 1][ship_col] = "x"
            battleship[ship_row + 2][ship_col] = "x"

def create_battleship2():
    "create a second battleship with the size of 2x1 with 50% chance being horizontal and 50% being vertical, also, if the random location chosen overlaps with the first battleship or goes out of boundary, it will return a zero, otherwise the function will return a 1"
    ship_row = generate_random_row(board)
    ship_col = generate_random_col(board)
    if decides_direction() == 0:
        if (ship_col or ship_row > 3):
            return 0;
        elif ((battleship[ship_row][ship_col] == "x") or (battleship[ship_row][ship_col + 1] == "x")):
            return 0;
        else:
            battleship[ship_row][ship_col] = "x"
            battleship[ship_row][ship_col + 1] = "x"
            return 1;
    else:
        if (ship_col or ship_row > 3):
            return 0;
        if ((battleship[ship_row][ship_col] == "x") or (battleship[ship_row + 1][ship_col] == "x")):
            return 0;
        else:
            battleship[ship_row][ship_col] = "x"
            battleship[ship_row + 1][ship_col] = "x"
            return 1;

def play_game():
    "starts the interaction with user and let the user take guesses of the location of battleship"
    
    turn = 1
    while turn < 5:
        print ("Let's play Battleship!")
        print('')
        print("Turn: " + str(turn))
        print('')
        print_board(board)
        print('')
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))
        print('')
        
        if (guess_row == 17 and guess_col == 17):
            print("okay, cheater. This is where the battleships are!")
            print_battleship(battleship)
            print('')
        elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            turn += 1
            print ("Oops, that's not even in the ocean. Extremely bad aim.")
            print('')
        
        elif battleship[guess_row][guess_col]== "x":
            print ("Congratulations! You sunk my battleship!")
            print ('')
            break
        else:
            turn += 1
            if(board[guess_row][guess_col] == "X"):
                print ("You guessed that one already, dummy.")
                print('')
            else:
                print ("You missed my battleship! HAHAHAHA You noob!")
                print('')
                board[guess_row][guess_col] = "X"
        if turn == 5:
            print("Game Over!")
            print('')

def main():
    create_boards()
    create_battleship1()
    condition = create_battleship2()
    while not (condition == 1):
        condition = create_battleship2()
    
    play_game()

# If this file, battleship.py, is run as a Python script (such as by typing
# "python election.py" at the command shell), then run the main() function.
if __name__ == "__main__":
    main()
