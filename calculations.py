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
        self.frees = list (range (9))

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

    def to_string (self):
        ans = ''
        for position in self.data.keys ():
            if position == 0 or position == 1 or position == 3 or position == 4 or position == 6 or position == 7:
                ans += " " + self.data[position] + " |"
            else:
                if position != 8:
                    ans += " " + self.data[position] + "\n-----------\n"
                else:
                    ans += " " + self.data[position]
        return ans

    def next_free (self):
        if len (self.frees) > 0:
            return self.frees[0]
        return None

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
                    self.frees.remove (spot)
                    self.moves += str (spot) + " x\n"
                    # self.print_board ()
                    # print ('\n')
                    self.generate_board (1, num_moves + 1)
                else:
                    self.data[spot] = "o"
                    self.frees.remove (spot)
                    self.moves += str (spot) + " o\n"
                    # self.print_board ()
                    # print ('\n')
                    self.generate_board (0, num_moves + 1)

def solve ():
    all_boards = set ()
    for i in range (9):
        b = Board ()
        b.data[i] = 'x'
        b.frees.remove (i)
        print ("I: ", i, "Num: ", solve_help (b, i, b.next_free (), 1, all_boards))
        print ("Len Allboards: ", len (all_boards))
        print ()

    return (len (all_boards))

def solve_help (board, start, position, turn, allboards):
    if position == None:
        return 0
    if position > 8 or board.check_win  ():
        allboards.add (board)
        return 1
        # new = Board ()
        # new.data[start] = 'x'
        # solve_help (new, start, 0, 1, allboards)
    else:
        if turn == 0:
            copee = copy.deepcopy(board)
            board.data[position] = 'x'
            board.frees.remove (position)
            ans = solve_help (board, start, board.next_free(), 1, allboards)
            for p in copee.frees:
                copee2 = copy.deepcopy (copee)
                return 1 + ans + solve_help (copee2, start, p, 1, allboards)
        else:
            copee = copy.deepcopy(board)
            board.data[position] = 'o'
            board.frees.remove (position)
            ans = solve_help (board, start, board.next_free(), 0, allboards)
            for p in board.frees:
                copee2 = copy.deepcopy(copee)
                return 1 + ans + solve_help (copee2, start, p, 0, allboards)



def generate_start (board, starting_position, position_now, turn, all_boards):
    if position_now > 8 or board.check_win ():
        all_boards.add (board.to_string())
        new = Board ()
        generate_start (new, starting_position + 1, 0, 0, all_boards)
    else:
        if board.data[position_now] != " ":
            generate_start (board, starting_position, position_now + 1, turn, all_boards)
        else:
            if turn == 0:
                board.data[position_now] = "x"
                generate_start (board, starting_position, position_now + 1, 1, all_boards)
                num = position_now
                while (num < 9):
                    generate_start (board, starting_position, num, 1, all_boards)
                    #generate_start (board, starting_position, num + 1, 0, all_boards)
                #generate_start (board, starting_position, position_now + 1, 1, all_boards)
                #generate_start (board, starting_position, position_now + 1, 0, all_boards)
            else:
                board.data[position_now] = "o"
                generate_start (board, starting_position, position_now + 1, 0, all_boards)
                num = position_now
                while (num < 9):
                    generate_start (board, starting_position, num, 0, all_boards)
                    #generate_start (board, starting_position, num + 1, 1, all_boards)
                #generate_start (board, starting_position, position_now + 1, 0, all_boards)
                #generate_start (board, starting_position, position_now + 1, 1, all_boards)

solve ()

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

# for i in range (9):
#     print ("Start: ", i)
#     new_board = Board ()
#     ab = set ()
#     generate_start (new_board, i, 0, ab)
#     for el in ab:
#         print (el)
#         print ()

# new_board = Board ()
# ab = set ()
# generate_start (new_board, 0,0,0,ab)
# print (len (ab))


# for el in ab:
#     print (el)
#     print ()
#unique_boards (1)

# a = Board()
# a.generate_board (0, 1)
# print (a.moves)
# a.print_board()
