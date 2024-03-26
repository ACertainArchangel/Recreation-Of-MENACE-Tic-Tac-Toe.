import numpy as np



def return_win(board):


    board = [[board[0],board[1],board[2]],
                [board[3],board[4],board[5]],
                [board[6],board[7],board[8]]]
    
    if board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X":
        return "X"
    if board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
        return "O"
    if board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X":
        return "X"
    if board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
        return "O"
    if board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
        return "O"
    if board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
        return "X"
    
    if board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
        return "X"
    if board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
        return "X"
    if board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
        return "X"
    if board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
        return "O"
    if board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O":
        return "X"
    if board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
        return "O"
        
    if board[1][1]=="X" and board[0][2]=="X" and board[2][0]=="X":
        return "X"
    if board[1][1]=="O" and board[0][2]=="O" and board[2][0]=="O":
        return "O"
    if board[1][1]=="X" and board[0][0]=="X" and board[2][2]=="X":
        return "X"
    if board[1][1]=="O" and board[0][0]=="O" and board[2][2]=="O":
        return "O"
    return 0

print(return_win(("N","N","X","N","N","X","N","N","X",)))