##Has run once


import json

import random as rand

Player_Starts_As_X = True ##STARTING (X) IS AI OR RANDOM/PLAYER. 

rigor = 100#255168 # Number of training moves

LOAD_A_FILE = True # ARE WE LOADING A MODEL? OR NEW?

WRITE_A_FILE = True #CREATE NEW / Train???

Loading_FileX = "DATA/DictionaryX.txt" # FROM WHICH FILE?

Loading_FileO = "DATA/DictionaryO.txt" # FROM WHICH FILE?

Playing = True # Are we not just training today?

Participation_Award = True #Logical value for rewarding ai for drawing

trainboth = True # Train both models???

####################################################################################################

if not Participation_Award:
    drawbonus = 0
elif Participation_Award:
    drawbonus = 1

def pack(index):


    string = ""
    for i in index:
        string = string + str(i) + "@"

    return string

def unpack(string, length=9):

    current_item = ""
    current_number = 0

    listus = [""]*length

    for character in string:
        if character!="@":
            current_item = current_item + character
        elif character == "@":

            try:
                listus[current_number] = int(current_item)

            except:
                listus[current_number] = str(current_item)

            current_number+=1
            current_item = ""


    return tuple(listus)

matchboxesX = {}

matchboxesO = {}

if not LOAD_A_FILE:
    matchboxesX = {"dummyyyyy": "variablee",
    }

    matchboxesO = {"dummyyyyy": "variablee",
    }

if LOAD_A_FILE:
    mx = json.load(open(Loading_FileX))

    for key in mx:
        lisht = []
        for item in mx[key]:
            try:
                lisht.append(int(item))
            except:
                lisht.append(str(item))
        toopul = tuple(lisht)
        matchboxesX[unpack(key)] = toopul

    mo = json.load(open(Loading_FileO))

    for key in mo:
        lisht = []
        for item in mo[key]:
            try:
                lisht.append(int(item))
            except:
                lisht.append(str(item))
        toopul = tuple(lisht)
        matchboxesO[unpack(key)] = toopul

    


board = ("N","N","N","N","N","N","N","N","N")


def random_move_as_x():

    learn()

    global board

    the_probability_distrabution = [""]*9

    the_probability_distrabution = list(the_probability_distrabution)

    board = list(board)
    for i in range(9):
        if board[i] == "N":
            the_probability_distrabution[i] = 1
        else:
            the_probability_distrabution[i] = 0
    board = tuple(board)
            

    the_probability_distrabution = tuple(the_probability_distrabution)

    choice = rand.choices(list(range(9)), the_probability_distrabution)

    board = list(board)
    board[choice[0]] = "X"
    board = tuple(board)






    learn()

def random_move_as_o():

    learn()

    global board

    the_probability_distrabution = [""]*9

    the_probability_distrabution = list(the_probability_distrabution)


    for i in range(9):
        if board[i] == "N":
            the_probability_distrabution[i] = 1

        else:
            the_probability_distrabution[i] = 0

            

    the_probability_distrabution = tuple(the_probability_distrabution)

    choice = rand.choices(list(range(9)), the_probability_distrabution)

    board = list(board)
    board[choice[0]] = "O"
    board = tuple(board)




    learn()

def ai_makes_move_as_x():

    learn()

    global board
    global matchboxesX

    has_found_board = False

    key = board
    
    if key in matchboxesX:
        if matchboxesX[key] == (0,0,0,0,0,0,0,0,0):
            the_probability_distrabution = [""]*9
            for i in range(9):
                if board[i] == "N":
                    the_probability_distrabution[i] = 2
                else:
                    the_probability_distrabution[i] = 0
            matchboxesX[key] = tuple(the_probability_distrabution)


        the_probability_distrabution = matchboxesX[key]

        choice = rand.choices(list(range(9)), matchboxesX[key])

        board = list(board)
        board[choice[0]] = "X"
        board = tuple(board)

        the_probability_distrabution = list(the_probability_distrabution)
        the_probability_distrabution[choice[0]] = str(the_probability_distrabution[choice[0]])+"A"
        the_probability_distrabution = tuple(the_probability_distrabution)

        matchboxesX[key] = the_probability_distrabution

        has_found_board = True



    if not has_found_board:
        the_probability_distrabution = [""]*9

        for i in range(9):
            if board[i] == "N":
                the_probability_distrabution[i] = 2
            else:
                the_probability_distrabution[i] = 0
            

        the_probability_distrabution = tuple(the_probability_distrabution)

        board = tuple(board)
        matchboxesX[board] = the_probability_distrabution

        key = board


        choice = rand.choices(list(range(9)), matchboxesX[key])

        board = list(board)
        board[choice[0]] = "X"
        board = tuple(board)

        the_probability_distrabution = list(the_probability_distrabution)
        the_probability_distrabution[choice[0]] = str(the_probability_distrabution[choice[0]])+"A"
        the_probability_distrabution = tuple(the_probability_distrabution)



def ai_makes_move_as_o():

    learn()

    global board
    global matchboxesO

    has_found_board = False

    key = board

    if key in matchboxesO:

        if matchboxesO[key] == (0,0,0,0,0,0,0,0,0):
            the_probability_distrabution = [""]*9
            for i in range(9):
                if board[i] == "N":
                    the_probability_distrabution[i] = 2
                else:
                    the_probability_distrabution[i] = 0
            matchboxesO[key] = tuple(the_probability_distrabution)


        the_probability_distrabution = matchboxesO[key]
        choice = rand.choices(list(range(9)), matchboxesO[key])
        board = list(board)
        board[choice[0]] = "O"
        board = tuple(board)
        the_probability_distrabution = list(the_probability_distrabution)
        the_probability_distrabution[choice[0]] = str(the_probability_distrabution[choice[0]])+"I"
        the_probability_distrabution = tuple(the_probability_distrabution)
        matchboxesO[key] = the_probability_distrabution
        has_found_board = True


    if not has_found_board:
        the_probability_distrabution = [""]*9

        for i in range(9):
            if board[i] == "N":
                the_probability_distrabution[i] = 2
            else:
                the_probability_distrabution[i] = 0
            

        the_probability_distrabution = tuple(the_probability_distrabution)

        board = tuple(board)
        matchboxesO[board] = the_probability_distrabution

        key = board
        choice = rand.choices(list(range(9)), matchboxesO[key])

        board = list(board)
        board[choice[0]] = "O"
        board = tuple(board)

        the_probability_distrabution = list(the_probability_distrabution)
        the_probability_distrabution[choice[0]] = str(the_probability_distrabution[choice[0]])+"I"
        the_probability_distrabution = tuple(the_probability_distrabution)


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

def learn():
    global board
    if (return_win(board) == 0) and "N" not in board:
        for key in matchboxesX:

            buildinglist = []
            for item in list(matchboxesX[key]):
                if str(item)[-1] == "A":
                    item = int(str(item)[:-1])+drawbonus
                buildinglist.append(item)
            matchboxesX[key] = tuple(buildinglist)

        

        for key in matchboxesO:

            buildinglistO = []
            for item in list(matchboxesO[key]):
                if str(item)[-1] == "I":
                    item = int(str(item)[:-1])+drawbonus
                buildinglistO.append(item)

            matchboxesO[key] = tuple(buildinglistO)

        board = ("N","N","N","N","N","N","N","N","N")


    elif return_win(board) == "X":
        for key in matchboxesX:
            buildinglist = []
            for item in list(matchboxesX[key]):
                if str(item)[-1] == "A":
                    item = int(str(item)[:-1])+2
                buildinglist.append(item)
            matchboxesX[key] = tuple(buildinglist)

        for key in matchboxesO:

            buildinglistO = []
            for item in list(matchboxesO[key]):
                if str(item)[-1] == "I":
                    item = int(str(item)[:-1])-1
                buildinglistO.append(item)
            matchboxesO[key] = tuple(buildinglistO)

        board = ("N","N","N","N","N","N","N","N","N")


    elif return_win(board) == "O":
        for key in matchboxesX:
            buildinglist = []
            for item in list(matchboxesX[key]):
                if str(item)[-1] == "A":
                    item = int(str(item)[:-1])-1
                buildinglist.append(item)
            matchboxesX[key] = tuple(buildinglist)

        for key in matchboxesO:

            buildinglistO = []
            for item in list(matchboxesO[key]):
                if str(item)[-1] == "I":
                    item = int(str(item)[:-1])+2
                buildinglistO.append(item)
            matchboxesO[key] = tuple(buildinglistO)

        board = ("N","N","N","N","N","N","N","N","N")

    try:
        for i in range(9):   
            if (board[i] != "N") and (matchboxesO[board][i]!=0):
                print("AAAAAAAAH!!!!")
                matchboxesO[board]=list(matchboxesO[board])
                matchboxesO[board][i]=0
                matchboxesO[board]=tuple(matchboxesO[board])
                
    except:
        pass

    try:
        for i in range(9):   
            if (board[i] != "N") and (matchboxesX[board][i]!=0):
                print("AAAAAAAAH!!!!")
                matchboxesX[board]=list(matchboxesX[board])
                matchboxesX[board][i]=0
                matchboxesX[board]=tuple(matchboxesX[board])
    except:
        pass

def finish_up_trainX():
    blin = True
    while blin:
        ai_makes_move_as_x()
        random_move_as_o()
        learn()
        if board==("N","N","N","N","N","N","N","N","N"):
            blin = False

def finish_up_trainO():
    blin = True
    while blin:
        ai_makes_move_as_o()
        random_move_as_x()
        learn()
        if board==("N","N","N","N","N","N","N","N","N"):
            blin = False
        
def train(rigour=1000, ai_starts = False, both=False):
    global board

    if both:
        for i in range(rigour):
            ai_makes_move_as_x()
            ai_makes_move_as_o()
            print("Progress:"+str(round(((100*(i))/(2*rigour)), 2))+"%                                 ",flush=True, end='\r')

        finish_up_trainX()

        board = ("N","N","N","N","N","N","N","N","N")

        for i in range(rigour):
            ai_makes_move_as_x()
            ai_makes_move_as_o()
            print("Progress:"+str(round(((100*(i+rigour))/(2*rigour)), 2))+"%                                 ",flush=True, end='\r')
            
        finish_up_trainO()

        board = ("N","N","N","N","N","N","N","N","N")



        

    elif ai_starts:

        for i in range(rigour):
            ai_makes_move_as_x()
            random_move_as_o()

            print("Progress:"+str(round((100*(i/rigour)), 2))+"%                                 ",flush=True, end='\r')

        finish_up_trainX()
        board = ("N","N","N","N","N","N","N","N","N")

    elif not ai_starts:
        for i in range(rigour):
            random_move_as_x()
            ai_makes_move_as_o()
            print("Progress:"+str(round((100*(i/rigour)), 2))+"%                                 ",flush=True, end='\r')
        finish_up_trainO()
        board = ("N","N","N","N","N","N","N","N","N")

from PIL import ImageTk, Image

def makemoveashuman(arg, human_first = True):
    global board 
    global NNN
    global OOO
    global XXX

    board = list(board)

    if human_first:
        board[arg] = "X"
        board = tuple(board)
        

        if return_win(board)=="X":
            YOUWIN()
            learn()
        elif return_win(board)=="O":
            AIWIN()
            learn()
        elif "N" not in board:
            DRAW()
            learn()

        ai_makes_move_as_o()

        if return_win(board)=="O":
            AIWIN()
            learn()
        elif return_win(board)=="X":
            YOUWIN()
            learn()
        elif ("N" not in board):
            DRAW()
            learn()

    elif not human_first:
        board[arg] = "O"
        board=tuple(board)

        if return_win(board)=="O":
            YOUWIN()
            learn()
        elif return_win(board)=="X":
            AIWIN()
            learn()
        elif ("N" not in board):
            DRAW()
            learn()

        ai_makes_move_as_x()

        if return_win(board)=="X":
            AIWIN()
            learn()
        elif return_win(board)=="O":
            YOUWIN()
            learn()
        elif ("N" not in board):
            DRAW()
            learn()


import easygui

import time

def YOUWIN():
    time.sleep(1)
    easygui.msgbox("YOU BEAT THE AI!!!", "Result", "Woo Hoo!!!")

def DRAW():
    time.sleep(1)
    easygui.msgbox("Draw", "Result", "Ok")

def AIWIN():
    time.sleep(1)
    easygui.msgbox("The AI mopped the floor with you...", "Result", "I'm a looser.")

train(rigour=rigor, ai_starts=(not Player_Starts_As_X), both=trainboth) ######################################################


for i in range(9):
    move = input("Move:")
    if move=="Q":
        break
    else:
        makemoveashuman(int(move),Player_Starts_As_X)
        print(board)
    


for key in matchboxesO:
    building = []
    for item in matchboxesO[key]:
        if str(item)[-1]=="A" or str(item)[-1]=="I":
            item = item[:-1]
        building.append(item)

    matchboxesO[key] = tuple(building)

for key in matchboxesX:
    building = []
    for item in matchboxesX[key]:
        if str(item)[-1]=="A" or str(item)[-1]=="I":
            item = item[:-1]
        building.append(item)
        
    matchboxesX[key] = tuple(building)


if WRITE_A_FILE:
    mx = {}

    for key in matchboxesX:
        mx[pack(key)] = matchboxesX[key]

    mo = {}

    for key in matchboxesO:
        mo[pack(key)] = matchboxesO[key]

    json.dump(mx, open(Loading_FileX,'w'))

    json.dump(mo, open(Loading_FileO,'w'))



    quit()






