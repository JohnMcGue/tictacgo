'''
Created on Aug 18, 2017

@author: johnm
'''
import random

class Node:
    def __init__(self, moveDict):
        self.moveDict = moveDict
    
    def getAction(self,game):
        return self.moveDict[tuple(game)]
    
def getAction(game):
    print(game)
    return int(input("Enter something: "))

def checkVictory(game):
    list1 = []
    lastPlay = game[len(game)-1]
    i = len(game)-3
    while i > -1:
        list1.append(game[i])
        i = i-2
    if lastPlay == 0:
        if (1 in list1 and 2 in list1) or (3 in list1 and 6 in list1) or (4 in list1 and 8 in list1):
            return True
    if lastPlay == 1:
        if (0 in list1 and 2 in list1) or (4 in list1 and 7 in list1):
            return True
    if lastPlay == 2:
        if (0 in list1 and 1 in list1) or (5 in list1 and 8 in list1) or (4 in list1 and 6 in list1):
            return True
    if lastPlay == 3:
        if (1 in list1 and 6 in list1) or (4 in list1 and 5 in list1):
            return True
    if lastPlay == 4:
        if (3 in list1 and 5 in list1) or (1 in list1 and 7 in list1) or (0 in list1 and 8 in list1) or (2 in list1 and 6 in list1):
            return True
    if lastPlay == 5:
        if (3 in list1 and 4 in list1) or (2 in list1 and 8 in list1):
            return True
    if lastPlay == 6:
        if (0 in list1 and 3 in list1) or (7 in list1 and 8 in list1) or (4 in list1 and 2 in list1):
            return True
    if lastPlay == 7:
        if (6 in list1 and 8 in list1) or (1 in list1 and 4 in list1):
            return True
    if lastPlay == 8:
        if (6 in list1 and 7 in list1) or (5 in list1 and 2 in list1) or (4 in list1 and 0 in list1):
            return True
    return False

numDict = {():random.randrange(9)}
for i in range(9):
    numDict[(i)] = random.randrange(9)
    for j in range(1,9):
        numDict[(i,j)] = random.randrange(9)
        for k in range(2,9):
            numDict[(i,j,k)] = random.randrange(9)
            for a in range(3,9):
                numDict[(i,j,k,a)] = random.randrange(9)
                for b in range(4,9):
                    numDict[(i,j,k,a,b)] = random.randrange(9)
                    for c in range(5,9):
                        numDict[(i,j,k,a,b,c)] = random.randrange(9)
                        for d in range(6,9):
                            numDict[(i,j,k,a,b,c,d)] = random.randrange(9)
                            for e in range(7,9):
                                numDict[(i,j,k,a,b,c,d,e)] = random.randrange(9)
                                for f in range(8,9):
                                    numDict[(i,j,k,a,b,c,d,e,f)] = random.randrange(9)
print(numDict)
node1 =  Node(numDict)
game = []
action = node1.getAction(game)
game.append(action)
for i in range(4):
    action = getAction(game)
    if action not in game:
        game.append(action)
    else:
        print("fail")
victory = checkVictory(game)
i=0
while not victory and i < 4:
    action = getAction(game)
    if action not in game:
        game.append(action)
    else:
        print("fail")
    victory = checkVictory(game)
    i = i+1
print("game over")