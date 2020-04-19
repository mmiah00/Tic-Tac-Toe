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
            if self.layout[Wins[0]] == self.layout[Wins[1]] and self.layout[Wins[1]] == self.layout[Wins[2]] and self.layout[Wins[0]] == self.layout[Wins[2]]:
                self.endState = self.layout[Wins[0]]
                return True
        return False

def next_open (layout):
    return layout.find ('_')

def all_opens (layout):
    ans = []
    for i in range (9):
        if layout[i] == '_':
            ans.append[i]
    return ans

def CreateAllBoards (layout, parent): #parent is a BoardNode
    board = BoardNode (layout)
    if board.checkwin ():
        AllBoards[layout] = board
    if '_' not in layout: #finished board
        parent.endState = 'd'
        AllBoards[layout] = board
    else:
        opens = all_opens (layout)
        for position in all_opens:
            if layout.count ('x') > layout.count ('o'):
                b = copy.copy (board)
                parent.children.add (b)
                b.layout[position] = 'o'
                CreateAllBoards (b.layout, board)
            else:
                b = copy.copy (board)
                parent.children.add (b)
                b.layout[position] = 'x'
                CreateAllBoards (b.layout, board)

CreateAllBoards ('_________', BoardNode ('_________'))
print (len (AllBoards))

    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary
