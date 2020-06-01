"""
@Author : Neeraj Deshpande
 Date: 3 May 2020
@GitHub ID : deshpandeneeraj
 GitHub Link : https://github.com/deshpandeneeraj/TicTacToeMinMax
"""

import random

def display(board):
    for row in board:
        print("\t", row)

#Check if any spot is empty
def moves_left(board):
    for row in board:
        for cell in row:
            if cell == "_":
                return True
            else:
                continue
            return False

#Evaluate current state of board
def evaluate(board):
    #Horizontal Win
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] == "x":
                return 10
            elif row[0] == "o":
                return -10
    #Vertical Win
    for col in range(3):
        if board[0][col] ==  board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == "x":
                return 10
            elif board[0][col] == "o":
                return -10
    #Diagonal Win
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == "x":
            return +10
        elif board[0][0] == "o":
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == "x":
            return +10
        elif board[0][2] == "o" :
            return -10
    #No win
    return 0

#Recursive Function for Finding Best Move Value
def minmax(board, depth, is_max):
    score = evaluate(board)
    if score == 10:
        return score
    elif score == -10:
        return score
    if not moves_left(board):
        return 0

    if is_max:
        temp = board.copy()
        best = -999
        for i, row in enumerate(temp):
            for j, cell in enumerate(row):
                if cell == "_":
                    temp[i][j] = "x"
                    move_score = evaluate(temp)
                    not_is_max = not is_max
                    best = max(best,
                        minmax(temp, depth+1, not_is_max))

                    temp[i][j] = "_"
        best -= depth
        return best
    else:
        temp = board.copy()
        best = +999
        for i, row in enumerate(temp):
            for j, cell in enumerate(row):
                if cell == "_":
                    temp[i][j] = "o"
                    move_score = evaluate(temp)
                    best = min(best,
                        minmax(temp, depth+1, is_max))
                    temp[i][j] = "_"
        best += depth
        return best

#Function that calls recursive function
def findBestMove(board, is_max):
    best_row = -1
    best_col = -1
    temp = board.copy()
    if is_max:
        best_value = -1000

        # Traverse all cells, evaluate minimax function for
        #  all empty cells. And return the cell with optimal
        #  value.
        for i in range(3):
            for j in range(3):
                #Check if cell is empty
                if temp[i][j]=='_':
                    # Make the move
                    temp[i][j] = "x"
                    move_value = minmax(temp, 0, False)

                    temp[i][j] = '_'

                    if move_value > best_value:
                        best_row = i
                        best_col = j
                        best_value = move_value
        return best_value, best_row, best_col
    else:
        best_value = 1000


        # Traverse all cells, evaluate minimax function for
        #  all empty cells. And return the cell with optimal
        #  value.
        for i in range(3):
            for j in range(3):
                #Check if cell is empty
                if temp[i][j]=='_':
                    # Make the move
                    temp[i][j] = "o"

                    move_value = minmax(temp, 0, True)

                    temp[i][j] = '_'

                    if move_value < best_value:
                        best_row = i
                        best_col = j
                        best_value = move_value

        return best_value, best_row, best_col

def ai_v_ai(board):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    print(f"Random First X at ({row}, {col})")
    board[row][col] = "x"
    display(board)

    turn = False
    while moves_left(board):
        if not turn:
            best_value, best_row, best_col = findBestMove(board, False)
            print("The value of the best Move for Y is :", best_value, best_row, best_col)
            board[best_row][best_col] = "o"
            turn = not turn

        else:
            best_value, best_row, best_col = findBestMove(board, True)
            print("The value of the best Move for X is :", best_value, best_row, best_col)
            board[best_row][best_col] = "x"
            turn = not turn


        display(board)
        if evaluate(board) == 10:
            print("X Won!")
            break
        elif evaluate(board) == -10:
            print("O Won!")
            break
    return board

def player_v_ai(board):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    print(f"Random First X at ({row}, {col})")
    board[row][col] = "x"
    display(board)
    turn = False
    while moves_left(board):
        if not turn:
            print("YOUR TURN")
            row = int(input("Enter Row(1-3): "))
            col = int(input("Enter Collumn(1-3): "))
            row -= 1
            col -= 1
            if board[row][col] == "_":
                print(f"Putting an O on ({row}, {col})")
                board[row][col] = "o"
                turn = not turn
            else:
                print("Can't play there!")
        else:
            best_value, best_row, best_col = findBestMove(board, True)
            print("The value of the best Move for AI is :", best_value, best_row, best_col)
            board[best_row][best_col] = "x"
            turn = not turn

        display(board)
        if evaluate(board) == 10:
            print("AI Won!")
            break

        elif evaluate(board) == -10:
            print("You Won!")
            break
    return board

if __name__ == "__main__":
    board = [["_","_","_"], ["_","_","_"],["_","_","_ "]]

    choice = input("Do you want to Play or let AI play with AI (y,n)")
    if choice.lower().startswith("y"):
        board = player_v_ai(board)
    elif choice.lower().startswith("n"):
        board = ai_v_ai(board)
    else:
        print("Wrong Choice!")
    print(f"Output Value = {evaluate(board)}\n Final State:")
    for row in board:
        print(row)
