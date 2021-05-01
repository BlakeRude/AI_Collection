"""
Author: Blake Rude

Minimax Algorithm implementation
to create an AI which plays
connect four with the user by trying to find
optimal moves

V1.0 -  5 June 2020
"""
import copy

rows = 6
cols = 7

board = [[' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],]

def welcome():
    print(" ________________________")
    print("|Welcome to Connect Four!", end = "|\n")
    print(" ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞")
    print("Programmed by: Blake Rude ")
    print("T represents the Human Player\nX represents the AI")
    
def printBoard(b):
    for r in b:
        for v in r:
            print(v, end = "|")
        print()
    print("0 1 2 3 4 5 6   Row Input")

def evalBoard(b):
    countx = 0
    countt = 0
    # Horizontal Check
    for r in b:
        for v in r:
            # Horizontal Check
            if(v == 'X'):
                countx += 1
                countt = 0
            elif(v == 'T'):
                countt += 1
                countx = 0
            else:
                countt = countx = 0
            if(countx == 4):
                return 1 # X is the AI, 1 is a win
            if(countt == 4):
                return -1 # T is the Player, -1 is lose
    # AI Diagonal Check
    for r in range(0, rows):
        for c in range(0, cols):
            if(b[r][c] == 'X'):
                countx +=1
                #NW Diagonal
                if(r-1 > 0 and c-1 > 0):
                    if(b[r-1][c-1] =='X'):
                        countx +=1
                        if(r-2 > 0 and c-2 > 0):
                            if(b[r-2][c-2] =='X'):
                                countx +=1
                                if(r-3 > 0 and c-3 > 0):
                                   if(b[r-3][c-3] =='X'):
                                       return 1
                                   else:
                                       countx = 1
                countx = 1
                #NE Diagonal
                if(r-1 > 0 and c+1 < cols):
                    if(b[r-1][c+1] =='X'):
                        countx +=1
                        if(r-2 > 0 and c+2 < cols):
                            if(b[r-2][c+2] =='X'):
                                countx +=1
                                if(r-3 > 0 and c+3 < cols):
                                   if(b[r-3][c+3] =='X'):
                                       return 1
                                   else:
                                       countx = 1
            countx = 0
        # Player Diagonal Check
#    for r in range(0, rows):
#        for c in range(0, cols):
            if(b[r][c] == 'T'):
                countt +=1
                #NW Diagonal
                if(r-1 > 0 and c-1 > 0):
                    if(b[r-1][c-1] =='T'):
                        countt +=1
                        if(r-2 > 0 and c-2 < 0):
                            if(b[r-2][c-2] =='T'):
                                countt +=1
                                if(r-3 > 0 and c-3 > 0):
                                   if(b[r-3][c-3] =='T'):
                                       return -1
                                   else:
                                       countt = 1
                countt = 1
                #NE Diagonal
                if(r-1 > 0 and c+1 < cols):
                    if(b[r-1][c+1] =='T'):
                        countt +=1
                        if(r-2 > 0 and c+2 < cols):
                            if(b[r-2][c+2] =='T'):
                                countt +=1
                                if(r-3 > 0 and c+3 < cols):
                                   if(b[r-3][c+3] =='T'):
                                       return -1
                                   else:
                                       countt = 1
            countt = 0
    #AI Vertical                                   
#    for r in range(0, rows):
#        for c in range(0, cols):
            if(b[r][c] == 'X'):
                countx +=1
                #Top Neighbor
                if(r-1 > 0):
                    if(b[r-1][c] =='X'):
                        countx +=1
                        if(r-2 > 0):
                            if(b[r-2][c] =='X'):
                                countx +=1
                                if(r-3 > 0):
                                   if(b[r-3][c] =='X'):
                                       return 1
                                   else:
                                       countx = 1
            countx = 0
            
            
    #Player Vertical                                   
#    for r in range(0, rows):
 #       for c in range(0, cols):
            if(b[r][c] == 'T'):
                countt +=1
                #Top Neighbor
                if(r-1 > 0):
                    if(b[r-1][c] =='T'):
                        countt +=1
                        if(r-2 > 0):
                            if(b[r-2][c] =='T'):
                                countt +=1
                                if(r-3 > 0):
                                   if(b[r-3][c] =='T'):
                                       return -1
                                   else:
                                       countt = 1
            countt = 0
    return 0 # no win or lose
            
                


def move(char):
    m = None
    while(m == None or m >= cols or m < 0 or board[0][m] != ' '):
        m = int(input("Move: "))
    makeMove(board, m, char)
    
def makeMove(b, col, char): #given board column character
    for r in range(5, -1, -1): # Limit is never reached in python
        if(b[r][col] == ' '):
            b[r][col] = char
            return

def chooseMove(b):
    bestmove = None
    bestvalue = float("-inf")
    for c in range(0, cols):
        if(b[0][c] == ' '): #make sure column isnt full
            value = mini(b, c, 1) # mini(current board, column, deapth)
            #print(str(c)+ " value = " + str(value))
            if(value > bestvalue):
                bestvalue = value
                bestmove = c
    return bestmove


maxdepth = 6
def mini(b, c, depth):
    newb = copy.deepcopy(b)
    makeMove(newb, c, 'X') # Place AI piece
    s = evalBoard(newb)
    if (s == 1):
        return 1
    if (s == -1):
        return -1
    if(depth == maxdepth):
        return s #currently always returns 0
    worstvalue = float('inf')
    for c in range(0, cols):
        if(b[0][c] == ' '): # make sure col is empty
            value = maxi(newb, c, depth+1)
            if (value < worstvalue):
                worstvalue = value
    return worstvalue
    
def maxi(b, c, depth):
    newb = copy.deepcopy(b)
    makeMove(newb, c, 'T') # Place AI piece
    s = evalBoard(newb)
    if (s == 1):
        return 1
    if (s == -1):
        return -1
    if(depth == maxdepth):
        return s #currently always returns 0
    bestvalue = float('-inf')
    for c in range(0, cols):
        if(b[0][c] == ' '): # make sure col is empty
            value = mini(newb, c, depth+1)
            if (value > bestvalue):
                bestvalue = value
    return bestvalue

# Start of Program
welcome()
while(True):
    WhosFirst = int(input("Who will start first? 0 for AI, 1 for Player (You)\n"))
    if(WhosFirst == 1 or WhosFirst == 0):
        break
    else:
        print("Incorrect input. Try a 0 or a 1.")
        
printBoard(board)
print()
for i in range(0, 10):
    if (not WhosFirst):
        #print("AI GOES FIRST")
        #move('X') # AI 
        print("AI is Thinking...")
        mv = chooseMove(board)
        makeMove(board,mv,'X')
        printBoard(board) #removable
        w = evalBoard(board)
        if (w == 1):
            print('AI Wins')
            break
        move('T') #PLAYER 
        printBoard(board) 
        w = evalBoard(board)
        if( w == -1):
            print('Player Wins')
            break
    elif (WhosFirst):
        #print("Player GOES FIRST")
        move('T') #PLAYER
        printBoard(board) 
        w = evalBoard(board)
        if( w == -1):
            print('Player Wins')
            break
        #move('X') # AI
        print("AI is Thinking...")
        mv = chooseMove(board)
        makeMove(board,mv,'X')
        printBoard(board)
        w = evalBoard(board)
        if (w == 1):
            print('AI Wins')
            break
    else:
        print("Fatal Error: Closing program")
        quit()

