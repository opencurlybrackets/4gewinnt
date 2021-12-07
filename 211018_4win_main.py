"""
Schutz vor "list index out of range"
 ---> Colum is full
 ---> mit range arbeiten
 2 player mit variable arbeiten
print(matrix[::-1])
"""

matrix = [
    ["00", "01", "02", "03", "04", "05", "06"],
    ["10", "11", "12", "13", "14", "15", "16"],
    ["20", "21", "22", "23", "24", "25", "26"],
    ["30", "31", "32", "33", "34", "35", "36"],
    ["40", "41", "42", "43", "44", "45", "46"],
    ["50", "51", "52", "53", "54", "55", "56"],
]
play = True


# various checks for winner

def diagonal_win_left_top(player):
    count = 0
    for column in range(0, 4):
        for row in range(0, 3):             # begin to look after a player token on position "50"
            if matrix[row][column] == player:
                for token in range(4):             # begin to check, if the token begins a connect4
                    if matrix[row + token][column + token] == player:   # check if their are other player tokens on the up right diagonal
                        count += 1
                    if count == 4:
                        return False
                else:
                    count = 0
    return True


def diagonal_win_left_bottom(player):
    count = 0
    for column in range(0, 4):
        for row in range(3, 6):             # begin to look after a player token on position "50"
            if matrix[row][column] == player:
                for token in range(4):             # begin to check, if the token begins a connect4
                    if matrix[row - token][column + token] == player:   # check if their are other player tokens on the up right diagonal
                        count += 1
                    if count == 4:
                        return False
                else:
                    count = 0
    return True


def column_win(player):
    count = 0
    for column in range(7):
        count = 0
        for row in range(6):
            if matrix[row][column] == player:
                print("+")
                count += 1
                if count == 4:
                    print("4 in a ROW")
                    return False
            else:
                print("-")
                count = 0
    return True


def row_win(player):
    # count = 0
    print("start")
    for row in range(6):
        count = 0
        for column in range(7):
            print(row, column)
            if matrix[row][column] == player:
                print("+")
                count += 1
                if count == 4:
                    print("4 in a ROW")
                    return False
            else:
                print("-")
                count = 0
    return True


# game loop
# to be added:
# - If a player attempts to place a disc in a column that is full then you should return ”Column full!”
#   and the next move must be taken by the same player.
# - If the game has been won by a player, any following moves should return ”Game has finished!”.
winner = ""
turn = 1
y = 5
while play:
    if turn % 2 != 0:
        inputP1 = int(input("Player 1 "))
        while matrix[y][inputP1] == "P2" or matrix[y][inputP1] == "P1":
            y -= 1
        matrix[y][inputP1] = "P1"
    elif turn % 2 == 0:
        inputP2 = int(input("Player 2 "))
        while matrix[y][inputP2] == "P2" or matrix[y][inputP2] == "P1":
            y -= 1
        matrix[y][inputP2] = "P2"
    y = 5
    turn += 1
    print(matrix)
    if not row_win("P1"):
        winner = "Player 1!"
        play = False
    # play = True if (play or playerX_row_win("P2")) else False
    elif not row_win("P2"):
        play = False
        winner = "Player 2!"
    elif not column_win("P1"):
        play = False
        winner = "Player 1!"
    elif not column_win("P2"):
        play = False
        winner = "Player 2!"
    elif not diagonal_win_left_bottom("P1"):
        play = False
        winner = "Player 1!"
    elif not diagonal_win_left_bottom("P2"):
        play = False
        winner = "Player 2!"
    elif not diagonal_win_left_top("P1"):
        play = False
        winner = "Player 1!"
    elif not diagonal_win_left_top("P2"):
        play = False
        winner = "Player 2!"
    print(play)
    for element in matrix:
        print(element)
print(f"Player {winner} wins!")
