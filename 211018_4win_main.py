'''
Schutz vor "list index out of range"
 ---> Colum is full
 ---> mit range arbeiten
 2 player mit variable arbeiten
print(matrix[::-1])
'''
matrix = [
["00","01","02","03","04","05","06"],
["10","11","12","13","14","15","16"],
["20","21","22","23","24","25","26"],
["30","31","32","33","34","35","36"],
["40","41","42","43","44","45","46"],
["50","51","52","53","54","55","56"],
]
play = True

def playerX_diagonal_win_2(playerX):
    count = 0

    for colum in range(6):
        n = 3
        print("XXXXXXXXXXXXXXXXXXXXXXXXXX")
        for row in range(6):
            print("------")
            if colum+n < 0:
                print("reset count")
                count = 0
            try:
                print(f"{colum + n}colum+n {row}row")
                print(matrix[row][colum + n])
                if matrix[row][colum+n] == playerX:
                    count += 1
                    print(f"++ {count} count")
                    if count == 4:
                        print("4 in a ROW")

                        return False

                else:
                    print("-")
                    count = 0
            except IndexError:
                print (IndexError)
            n -= 1
        print("diagonal")
    return True

def playerX_diagonal_win(playerX):
    count = 0

    for colum in range(6):
        n = -2
        for row in range(6):
            if colum+n == 0:
                count = 0
            try:
                if matrix[row][colum+n] == playerX:
                    print("+")
                    count += 1
                    if count == 4:
                        print("4 in a ROW")

                        return False

                else:
                    print("-")
                    count = 0
            except IndexError:
                print (IndexError)
            n += 1
        print("diagonal")
    return True

def playerX_colum_win(playerX):
    count = 0
    for colum in range(7):
        count = 0
        for row in range(6):
            if matrix[row][colum] == playerX:
                print("+")
                count += 1
                if count == 4:
                    print("4 in a ROW")

                    return False

            else:
                print("-")
                count = 0
    return True


def playerX_row_win(playerX):
    #count = 0
    print("start")
    for row in range(6):
        count = 0
        for index in range(7):
            print(row, index)

            if matrix[row][index] == playerX:
                print("+")
                count +=1
                if count == 4:
                    print("4 in a ROW")

                    return False

            else:
                print("-")
                count = 0
    return True

winner = ""
turn = 1
y = 5
while play == True:
    if turn % 2 != 0:
        inputP1 = int(input("_"))
        while matrix[y][inputP1] == "P2" or matrix[y][inputP1] == "P1":
            y -= 1
        matrix[y][inputP1] = "P1"
    elif turn % 2 == 0:
        inputP2 = int(input("_"))
        while matrix[y][inputP2] == "P2" or matrix[y][inputP2] == "P1":
            y -= 1
        matrix[y][inputP2] = "P2"
    y = 5
    turn += 1
    if playerX_row_win("P1") == False:
        winner = "Player 1!"
        play = False
    #play = True if (play or playerX_row_win("P2")) else False
    elif playerX_row_win("P2") == False:
        play = False
        winner = "Player 2!"
    elif playerX_colum_win("P1") == False:
        play = False
        winner = "Player 1!"
    elif playerX_colum_win("P2") == False:
        play = False
        winner = "Player 2!"
    elif playerX_diagonal_win("P1") == False:
        play = False
        winner = "Player 1!"
    elif playerX_diagonal_win("P2") == False:
        play = False
        winner = "Player 2!"
    elif playerX_diagonal_win_2("P1") == False:
        play = False
        winner = "Player 1!"
    elif playerX_diagonal_win_2("P2") == False:
        play = False
        winner = "Player 2!"

    print(play)
    for element in matrix:
        print(element)
print(f"[{winner} has won the game!")
