#! /usr/bin/python3
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

    def to_string (self):
        ans = ''
        for pos in self.data.keys ():
            if self.data[pos] == " ":
                ans += '_'
            else:
                ans += self.data[pos]
        return ans


def ABC(): #answers to parts a, b, and c
    total_games = 0
    total_strings = set()
    total_boards = set ()
    o_wins = 0
    x_wins = 0
    draws = 0
    for x1 in range(9):
        first = Board()
        available1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        available2 = available1[:]
        available2.remove(x1)
        first.data[x1] = 'x'

        if first.to_string () not in total_strings:
            total_strings.add(first.to_string ())
            total_boards.add (first)
        for o1 in available2:
            second = copy.deepcopy (first)
            available3 = available2[:]
            available3.remove(o1)

            second.data[o1] = 'o'

            if second.to_string () not in total_strings:
                total_strings.add(second.to_string ())
                total_boards.add (second)
            for x2 in available3:
                third = copy.deepcopy (second)
                available4 = available3[:]
                available4.remove(x2)

                third.data[x2] = 'x'

                if third.to_string () not in total_strings:
                    total_strings.add(third.to_string ())
                    total_boards.add (third)
                for o2 in available4:
                    fourth = copy.deepcopy (third)
                    available5 = available4[:]
                    available5.remove(o2)

                    fourth.data[o2] = 'o'

                    if fourth.to_string () not in total_strings:
                        total_strings.add(fourth.to_string ())
                        total_boards.add (fourth)
                    for x3 in available5:
                        fifth = copy.deepcopy (fourth)
                        available6 = available5[:]
                        available6.remove(x3)

                        fifth.data[x3] = 'x'

                        if first.to_string () not in total_strings:
                            total_strings.add(fifth.to_string ())
                            total_boards.add (fifth)
                        if fifth.check_win ():
                            total_games += 1
                            x_wins+=1
                        else:
                            for o3 in available6:
                                sixth = copy.deepcopy (fifth)
                                available7 = available6[:]
                                available7.remove(o3)

                                sixth.data[o3] = 'o'

                                if sixth.to_string () not in total_strings:
                                    total_strings.add(sixth.to_string ())
                                    total_boards.add (sixth)
                                if sixth.check_win ():

                                    total_games+=1
                                    o_wins+=1
                                else:
                                    for x4 in available7:
                                        seventh = copy.deepcopy (sixth)
                                        available8 = available7[:]
                                        available8.remove(x4)

                                        seventh.data[x4] = 'x'

                                        if seventh.to_string () not in total_strings:
                                            total_strings.add(seventh.to_string ())
                                            total_boards.add (seventh)
                                        if seventh.check_win ():

                                            total_games += 1
                                            x_wins+=1
                                        else:
                                            for o4 in available8:
                                                eigth = copy.deepcopy (seventh)
                                                available1 = available2[:]
                                                available1.remove(o4)
                                                eigth.data[o4] = 'o'

                                                if eigth.to_string () not in total_strings:
                                                    total_strings.add(eigth.to_string ())
                                                    total_boards.add (eigth)
                                                if eigth.check_win ():

                                                    total_games+=1
                                                    o_wins+=1
                                                else:
                                                    eigth.data[available1[0]] = 'x'

                                                    if first.to_string () not in total_strings:
                                                        total_strings.add(eigth.to_string ())
                                                        total_boards.add (eigth)
                                                    if eigth.check_win ():

                                                        x_wins+=1
                                                    else:
                                                        draws+=1
                                                    total_games+=1
    print ("Total Games: ", total_games, "\nX Won ", x_wins, "times\nO Won ", o_wins, "times\nDraw ", draws, " times\nDifferent Configurations: ", len (total_strings))
    return total_boards, total_strings

def make_transformation (board, transformation):
    ans = Board ()
    for i in range (8):
        val = board.data[i]
        ans.data[transformation[i]] = val
        # ans.print_board ()
        # print ()
    return ans

def without_transformation(set_boards, set_strings):
    Rot90 = [6,3,0,7,4,1,8,5,2]
    Rot180 = [8,7,6,5,4,3,2,1,0]
    Rot270 = [2,5,8,1,4,7,0,3,6]
    VertFlip= [2,1,0,5,4,3,8,7,6]
    Transformations = [[Rot90],[Rot180],[Rot270],[VertFlip],[Rot90,VertFlip],[Rot180,VertFlip],[Rot270,VertFlip]]

    b = copy.copy (set_strings)
    ans = set()
    for board in set_boards:
        r90 = make_transformation (board, Rot90)
        r180 = make_transformation (board, Rot180)
        r270 = make_transformation (board, Rot270)
        vert = make_transformation (board, VertFlip)
        r90vert = make_transformation (r90, VertFlip)
        r180vert = make_transformation (r180, VertFlip)
        r270vert = make_transformation (r270, VertFlip)

        r90_string = r90.to_string ()
        r180_string = r180.to_string ()
        r270_string = r270.to_string ()
        vert_string = vert.to_string ()
        r90vert_string = r90vert.to_string ()
        r180vert_string = r180vert.to_string ()
        r270vert_string = r270vert.to_string ()
        if not (r90_string in b or r180_string in b or r270_string in b or vert_string in b or r90vert_string in b or r180vert_string in b or r270vert_string in b):
            ans.add (board)
        # if r90_string in b and r180_string in b and r270_string in b and vert_string in b and r90vert_string in b and r180vert_string in b and r270vert_string in b:
        #     ans.add (board)
    return ans

tb = ABC ()
print ("Without Transformations: ", len (without_transformation (tb[0], tb[1])))
