#! /usr/bin/python
import random
import sys
import time
import copy

class Board:
    cliques = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def __init__ (self):
        self.data = dict ()
        for i in range (9):
            self.data[i] = " "
        self.moves = ""
        self.winner = None

    def check_win (self):
        for clique in self.cliques:
            if (self.data[clique[0]] != " ") and (self.data[clique[1]] != " ") and (self.data[clique[2]] != " "):
                if (self.data[clique[0]] == self.data[clique[1]]) and (self.data[clique[1]] == self.data[clique[2]]) and (self.data[clique[0]] == self.data[clique[2]]):
                    #print ("Winner: ", self.data[clique[0]])
                    self.winner = self.data[clique[0]]
                    return True
        return False

    def print_board (self):
        ans = ''
        for position in self.data.keys ():
            if position == 0 or position == 1 or position == 3 or position == 4 or position == 6 or position == 7:
                ans += " " + self.data[position] + " |"
            else:
                if position != 8:
                    ans += " " + self.data[position] + "\n-----------\n"
                else:
                    ans += " " + self.data[position]
        print (ans)

    def generate_random (self, turn, num_moves): #generates a board using random values
        if num_moves > 9 or self.check_win (): #either ended in a draw or a single winner
            #print ("DONE")
            #print (num_moves)
            return True
        else:
            spot = random.randint (0,8)
            #print ("Turn: ", turn, 'Spot: ', spot)
            if self.data[spot] != " ": #filled
                self.generate_board (turn, num_moves) #try again
            else:
                if turn == 0:
                    self.data[spot] = "x"
                    self.moves += str (spot) + " x\n"
                    # self.print_board ()
                    # print ('\n')
                    self.generate_board (1, num_moves + 1)
                else:
                    self.data[spot] = "o"
                    self.moves += str (spot) + " o\n"
                    # self.print_board ()
                    # print ('\n')
                    self.generate_board (0, num_moves + 1)

def solve ():
    all_boards = set ()
    for i in range (9):
        solve_helper (Board (), i, 0, all_boards)

    print (len (all_boards))

def solve_helper (board, start_position, turn, allboards):
    if start_position >= 9 or board.check_win ():
        allboards.add (board)
        #return allboards
    else:
        if (board.data[start_position] == " "):
            if turn == 0:
                board.data[start_position] = "x"
                num = start_position
                while (num < 9):
                    solve_helper (board, num, 1, allboards)
                    num += 1
                #return solve_helper (board, start_position + 1, 1, allboards)
                #solve_helper (board, start_position + 2, 0, allboards)
            else:
                board.data[start_position] = "o"
                num = start_position
                while (num < 9):
                    solve_helper (board, num, 0, allboards)
                    num += 1
                #return solve_helper (board, start_position + 1, 0, allboards)
                #solve_helper (board, start_position + 2, 1, allboards)










all_boards = set () #key = board value = count
def unique_boards (num):
    x_wins = 0
    o_wins = 0
    draws = 0
    for i in range (1000000):
        a = Board ()
        a.generate_board (0, 1)
        if a.winner == 'x':
            x_wins += 1
        elif (a.winner == 'o'):
            o_wins += 1
        else:
            draws += 1
        all_boards.add (a.moves)
    #return len (all_boards)
    print ("Total Combinations: ", len (all_boards))
    print ("X Won ", x_wins, " times")
    print ("O Won ", o_wins, " times")
    print ("", draws, " Draws")
    # if a in all_boards:
    #     all_boards[a] += 1
    # else:
    #     all_boards[a] = 1
    # if 1 in all_boards.values():
    #     unique_boards (num + 1)
    # else:
    #     return num


#unique_boards (1)
solve ()

# a = Board()
# a.generate_board (0, 1)
# print (a.moves)
# a.print_board()
