import pyfiglet
import random
from termcolor import colored
import os
import time

os.system("color")
start_time = time.time()


def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()
    print("______________________________")


winner = 0


def check_game():
    global winner
    for i in range(3):
        if (game_board[i][0] == colored("X", "red") and game_board[i][1] == colored("X", "red") and game_board[i][2] == colored("X", "red")) \
                or (game_board[0][i] == colored("X", "red") and game_board[1][i] == colored("X", "red") and game_board[2][i] == colored("X", "red")):
            winner = 1

        elif (game_board[i][0] == colored("O", "blue") and game_board[i][1] == colored("O", "blue") and game_board[i][2] == colored("O", "blue")) \
                or (game_board[0][i] == colored("O", "blue") and game_board[1][i] == colored("O", "blue") and game_board[2][i] == colored("O", "blue")):
            winner = 2

    if (game_board[0][0] == colored("X", "red") and game_board[1][1] == colored("X", "red") and game_board[2][2] == colored("X", "red")) \
            or (game_board[0][2] == colored("X", "red") and game_board[1][1] == colored("X", "red") and game_board[2][0] == colored("X", "red")):
        winner = 1

    elif (game_board[0][0] == colored("O", "blue") and game_board[1][1] == colored("O", "blue") and game_board[2][2] == colored("O", "blue")) \
            or (game_board[0][2] == colored("O", "blue") and game_board[1][1] == colored("O", "blue") and game_board[2][0] == colored("O", "blue")):
        winner = 2

    elif not any("_" in x for x in game_board):
        winner = 3


first_title = pyfiglet.figlet_format("Tic Toc Toe", font="slant")
print(first_title)

print("Hold 1 for Play vs Computer")
print("Hold 2 for Play vs Friend")

while True:
    game_mode = int(input("Game Mode: "))
    if game_mode != 1 and game_mode != 2:
        print("Not an appropriate choice.")
    else:
        break


game_board = [["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]]
show()


if game_mode == 1:
    while True:
        print("Player 1")
        while True:
            row = int(input("row: "))
            column = int(input("column: "))
            if (0 <= row <= 2) and (0 <= column <= 2):
                if game_board[row][column] == "_":
                    game_board[row][column] = colored("X", "red")
                    break
                else:
                    print("Choose Un-taken Location")
            else:
                print("Enter Valid Location (0, 1, 2)")
        show()
        check_game()

        if not any("_" in x for x in game_board):
            break

        if winner == 1:
            break

        print("Computer")
        while True:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if (0 <= row <= 2) and (0 <= column <= 2):
                if game_board[row][column] == "_":
                    game_board[row][column] = colored("O", "blue")
                    break
                else:
                    continue
            else:
                continue
        show()
        check_game()
        if winner == 2:
            break


if game_mode == 2:
    while True:

        print("Player 1")
        while True:
            row = int(input("row: "))
            column = int(input("column: "))
            if (0 <= row <= 2) and (0 <= column <= 2):
                if game_board[row][column] == "_":
                    game_board[row][column] = colored("X", "red")
                    break
                else:
                    print("Choose Un-taken Location")
            else:
                print("Enter Valid Location (0, 1, 2)")
        show()
        check_game()

        if not any("_" in x for x in game_board):
            break

        if winner == 1:
            break

        print("Player 2")
        while True:
            row = int(input("row: "))
            column = int(input("column: "))
            if (0 <= row <= 2) and (0 <= column <= 2):
                if game_board[row][column] == "_":
                    game_board[row][column] = colored("O", "blue")
                    break
                else:
                    print("Choose Un-taken Location")
            else:
                print("Enter Valid Location (0, 1, 2)")

        show()
        check_game()
        if winner == 2:
            break


if winner == 1:
    print("Player I Wins")
elif winner == 2:
    if game_mode == 2:
        print("Player II Wins")
    elif game_mode == 1:
        print("Computer Wins")
elif winner == 3:
    print("Draw")

end_time = time.time()
print(f"The Execution time of the program is : {round((end_time - start_time), 3)} Seconds")
