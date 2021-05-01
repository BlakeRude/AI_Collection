"""
Blake Rude
CS 470
Project 3 - CSP Map
Due: 16 June 2020
"""

import copy
import random
import sys

sys.setrecursionlimit(10**6)

num = 30
numcolors = 4 # Change to whatever you please

#                          1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3
#        1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
map1 = [[0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], # X1
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0], # X2
        [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0], # X3
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1], # X4
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0], # X5
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0], # X6
        [0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], # X7
        [0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0], # X8
        [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0], # X9
        [0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], # X10
        [0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0], # X11
        [0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], # X12
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], # X13
        [0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1], # X14
        [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0], # X15
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], # X16
        [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], # X17
        [0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0], # X18
        [0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], # X19
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # X20
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0], # X21
        [0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1], # X22
        [0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0], # X23
        [0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], # X24
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0], # X25
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], # X26
        [0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], # X27
        [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0], # X28
        [1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1], # X29
        [0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0]] # X30

solution = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,] #-1 = no color
numedges = [4,3,7,3,4,4,3,5,4,5,7,4,3,7,6,1,4,6,3,1,4,8,4,5,4,2,4,3,9,6] # 1-30
def count_conflicts(m, sol):
    conflicts = 0
    for i in range(0, num):
        for j in range(i+1, num):
            if(m[i][j] == 1): # the regions are connected
                if(sol[i] == sol[j] and sol[i] != -1 and sol[j] != -1):
                    conflicts += 1
    return conflicts

def degreeheuristic(nEdges):
    maxi = -1
    keepi = -1
    for i in range(0,num):
        if nEdges[i] > maxi:
           maxi = nEdges[i]
           keepi = i
    nEdges[keepi] = 0
    #print("Max:",maxi,"\ni to recurse: ", keepi)
    return keepi
    

def fully_assigned(s):
    for i in range(0, len(s)):
        if (s[i] == -1):
            return False
    return True
    
def solutionsearch(s, var, nEdge): #(solution its currently working on(recursively), var we want to assign color to)
    for c in range(0, numcolors):
        s2 = copy.deepcopy(s)
        s2[var] = c
        print(var, s2, count_conflicts(map1, s2))
        if(count_conflicts(map1, s2) == 0): #no conflicts yet
            if(fully_assigned(s2) == True):
                return True
            else:
                maxi = degreeheuristic(nEdge)
                #print("max: ", maxi,"\nnEdge: ",nEdge)
                temp = solutionsearch(s2, maxi, nEdge) #var+1)
                if(temp == True):
                    return True
    return False # no solution

print("Constraint Satisfaction Problem Solver\nProgrammed by: Blake Rude")
print("This program will solve the given map problem and assign colors\n which do not conflict with the regions next to it")
choose = int(input("Press 0 for Local Search: Hill Climbing or\n1 for Global Search: BFS with Degree Heuristic\n"))
if choose == 0:
    print("Local Search: Hillclimbing chosen.")
    hcsol = copy.deepcopy(solution)
    for i in range(0, num):
        hcsol[i] = random.randint(0,numcolors-1)
    #print("Generated Solution:\n",hcsol)
    minconflicts = count_conflicts(map1, hcsol)
    #print("conflicts: ", minconflicts)
    prevsol = copy.deepcopy(hcsol)
    for i in range(0,num):
        for c in range(0,numcolors):
            newsol = copy.deepcopy(hcsol)
            newsol[i] = c
            numconflicts = count_conflicts(map1, newsol)
            if numconflicts < minconflicts:
                 hcsol = copy.deepcopy(newsol)
                 minconflicts = numconflicts
    print("Generated Solution:\n",hcsol)
    minconflicts = count_conflicts(map1, hcsol)
    print("conflicts: ", minconflicts)
elif choose == 1:
    print("Global Search: BFS with Degree Heuristic chosen")
    solutionsearch(solution,0,numedges)
else:
    print("Invalid Input")