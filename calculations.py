#! /usr/bin/python
import random

class Board:
    cliques = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def __init__ (self):
        self.data = dict ()
        for i in range (9):
            self.data[i] = " "
        self.moves = ""

    def check_win (self):
        for clique in self.cliques:
            if (self.data[clique[0]] != " ") and (self.data[clique[1]] != " ") and (self.data[clique[2]] != " "):
                if (self.data[clique[0]] == self.data[clique[1]]) and (self.data[clique[1]] == self.data[clique[2]]) and (self.data[clique[0]] == self.data[clique[2]]):
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
        print (ans)

    def make_board (self, turn, num_moves):
        if self.check_win () or num_moves == 9:
            return True
        else:
            spot = random.randint (0,8)
            if self.data[spot] != " ": #filled
                self.make_board (turn, num_moves) #try again
            else:
                if turn == 0:
                    self.data[spot] = "x"
                    self.make_board (1, num_moves + 1)
                else:
                    self.data[spot] = "o"
                    self.make_board (0, num_moves + 1)

a = Board()
a.make_board (0, 1)
a.print_board()
