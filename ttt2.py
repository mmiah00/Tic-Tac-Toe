#! /usr/bin/python3
import sys
import time
import copy

''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# layouts look like "_x_ox__o_"

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode

class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.children = [] # all layouts that can be reached with a single move

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('children:',self.children)

    def checkwin (self):
        for clique in Wins:
            if self.layout[clique[0]] != "_" and self.layout[clique[0]] == self.layout[clique[1]] and self.layout[clique[1]] == self.layout[clique[2]] and self.layout[clique[0]] == self.layout[clique[2]]:
                self.endState = self.layout[clique[0]]
                return True
        return False

def next_open (layout):
    return layout.find ('_')

def all_opens (layout):
    ans = []
    for i in range (9):
        if layout[i] == '_':
            ans.append(i)
    return ans

def replace (character, position, layout):
    s = list (layout)
    s[position] = character
    return "".join (s)

def CreateAllBoards (layout, parent): #parent is a BoardNode
    if layout not in AllBoards.keys (): #so it doesn't waste time w duplicates
        if parent.checkwin ():
            AllBoards[layout] = parent
        if '_' not in layout: #board w all spaces filled
            parent.endState = 'd'
            AllBoards[layout] = parent
        else:
            opens = all_opens (layout)
            for position in opens:
                b = copy.copy (parent)
                parent.children.append (b)
                if b.endState == None:
                    if layout.count ('x') == 0 or layout.count ('x') == layout.count ('o'): #x's turn
                        temp = b.layout
                        b.layout = replace ('x', position, temp)
                        CreateAllBoards (b.layout, b)
                    else: #o's turn
                        temp = b.layout
                        b.layout = replace ('o', position, temp)
                        CreateAllBoards (b.layout, b)
            AllBoards[layout] = parent


CreateAllBoards ('_________', BoardNode ('_________'))
x_wins = 0
o_wins = 0
draws = 0
nones = 0
for key in AllBoards.keys ():
    n = AllBoards[key]
    if n.endState == 'x':
        x_wins += 1
    elif n.endState == 'o':
        o_wins += 1
    elif n.endState == 'd':
        draws += 1
    else:
        nones += 1

print ("Total Boards ", len (AllBoards))
print ("X Wins       ", x_wins)
print ("O Wins       ", o_wins)
print ("Draws        ", draws)
print ("Nones        ", nones)
#print ("total: ", (x_wins + o_wins + draws + nones))


# print ("Total Boards ", len (AllBoards))
# print ("X Wins       ", len (x_wins))
# print ("O Wins       ", len (o_wins))
# print ("Draws        ", len (draws))
# print ("Nones        ", len (nones))
