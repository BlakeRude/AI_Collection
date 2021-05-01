"""
Blake Rude

Uses Pathfinding algorithms which find optimal path
in a given file, with a user chosen pathfinding algorithm
file MUST be of similar format to that of the provided
map.txt

V1.0 - 29 May 2020
"""
#import random
#import numpy
flag = 0
ij = 0
class cell:
    def __init__(self,x,y,sType):
        self.x = x
        self.y = y
        self.sType = sType
        if sType == 'R':
            self.cost = 1
        elif sType == 'f':
            self.cost = 2
        elif sType == 'F':
            self.cost = 4
        elif sType == 'h':
            self.cost = 5
        elif sType == 'r':
            self.cost = 7
        elif sType == 'M':
            self.cost = 10
        elif sType == 'W':
            self.cost = 100
        self.costtoreach = 0
        self.estimatedcosttogoal = 0
        self.parent = None
        self.pathlen = 1

    def __lt__(self,other):
        if search_pick == 2:# Least Cost
            if(self.costtoreach < other.costtoreach):
                return True
            return False
        elif search_pick == 3: # Greedy Best
            if(self.estimatedcosttogoal < other.estimatedcosttogoal):
                return True
            return False
        elif search_pick in [4,5]: # A*
            if(self.costtoreach+self.estimatedcosttogoal < other.costtoreach+other.estimatedcosttogoal):
                return True
            return False
        else:
            print("LESS THAN ERROR")
    
    def printPath(self):
        global ij
        print(self.sType)
        pathlist.append(self)
        ij= ij+1
        if(self.parent != None):
            #ij = ij+1
            self.parent.printPath()
        

print("Pathfinding Project.")
#print("\033[44;33mHello World!\033[m")
uInput = input("Give the name of the file you wish to pathfind.\n")

fo = open(uInput, "r")
width = fo.read(2)
fo.read(1)
height = fo.read(2)
fo.read(1)
StartX = fo.read(1)
fo.read(1)
StartY = fo.read(1)
fo.read(1)
GoalX = fo.read(1)
fo.read(1)
GoalY = fo.read(2)
fo.read(1)

pathlist = []
visitlist = []
characters = []
for i in range(0,int(height)):
    temp = (fo.read(int(width)))
    #print("Line ", i, ": ", temp)
    characters.append(temp)
    characters[i].split()
    fo.read(1)
#print(characters)
print("File Read.")
while(not flag):
    search_pick = int(input("Pick a search type:\n1 = Breadth First Search\n2 = Lowest Cost\n3 = Greedy Best First\n4 = A*\n"))
    if search_pick in [1,2,3,4,5]:
        flag = 1
    else:
        print("INVALID NUMBER")
map = []
for y in range (0,int(height)):
    r = []
    for x in range (0,int(width)):
        c = cell(x,y, characters[y][x])
        r.append(c)
    map.append(r)

searchmap = map
def printMap():
    for r in map:
        for c in r:
            print(c.sType, end = " ")
        print()
def printSearchedMap():
    for r in searchmap:
        for c in r:
            if c in pathlist:
                print("\033[44;33m", c.sType, "\033[m", end = " ")
            elif c in visitlist:
                print("\033[33;66m", c.sType, "\033[m", end = " ")
            else:
                print("\033[11;77m", c.sType, "\033[m", end = " ")
        print()
    print("Legend: Red Text = visited, Blue Highlight = Path, White = unvisited")
def searchList(thisList, item):
    for i in thisList:
        if i == item:
            return True
    return False

def printList(l):
    for i in l:
        print(i.sType, end = " ")
    print() #newline
    
openlist = []
closedlist = []

goal = map[5][10] # Interchangable

def search():
    start = map[0][5] # Interchangable
    start.costtoreach = start.cost
    start.parent = None
    openlist.append(start)
    while(len(openlist) > 0):
        if search_pick in [2,3,4,5]:
            openlist.sort()
        print("Open ", end = " ")
        printList(openlist)
        print("Closed ", end = " ")
        printList(closedlist)
        current = openlist.pop(0)
        visitlist.append(current)
        if (current == goal):
            print("Success")
            goal.printPath()
            print("Cost: ",goal.costtoreach)
            print("Path Length: ",ij)
            printSearchedMap()
            break
        closedlist.append(current)
        # find each neighbor of current
        # if a neighbor is not on the open or closed list,
        # add it to the openlist
        if ( current.x > 0 ): # Left neighbor
            neighbor = map[current.y][current.x-1]
            if( not searchList(openlist, neighbor) and not searchList(closedlist, neighbor) and not neighbor.sType == 'W'):
                neighbor.costtoreach = current.costtoreach + neighbor.cost
                neighbor.parent = current
                openlist.append(neighbor)
        if ( current.x < len(map[0])-1 ): # Right neighbor
            neighbor = map[current.y][current.x+1]
            if( not searchList(openlist, neighbor) and not searchList(closedlist, neighbor)and not neighbor.sType == 'W'):
                neighbor.costtoreach = current.costtoreach + neighbor.cost
                neighbor.parent = current
                openlist.append(neighbor)
        if ( current.y > 0 ): # Top neighbor
            neighbor = map[current.y-1][current.x]
            if( not searchList(openlist, neighbor) and not searchList(closedlist, neighbor)and not neighbor.sType == 'W'):
                neighbor.costtoreach = current.costtoreach + neighbor.cost
                neighbor.parent = current
                openlist.append(neighbor)
        if ( current.y < len(map)-1 ): # Bottom neighbor
            neighbor = map[current.y+1][current.x]
            if( not searchList(openlist, neighbor) and not searchList(closedlist, neighbor)and not neighbor.sType == 'W'):
                neighbor.costtoreach = current.costtoreach + neighbor.cost
                neighbor.parent = current
                openlist.append(neighbor)
search()
