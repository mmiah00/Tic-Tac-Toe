#! /usr/bin/python

cliques = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
possible_games = 0
data = dict ()
for i in range (9):
    data[i] = " "
moves = ""

def check_win ():
    for clique in cliques:
        if (data[clique[0]] == data[clique[1]]) and (data[clique[1]] == data[clique[2]]) and (data[clique[0]] == data[clique[2]]):
            return True
    return False

def print_board ():
    ans = ''
    for position in data.keys ():
        if position == 0 or position == 1 or position == 3 or position == 4 or position == 6 or position == 7:
            ans += " " + data[position] + " |"
        else:
            if position != 8:
                ans += " " + data[position] + "\n-----------\n"
    print (ans)

data[0] = "x"
data[1] = "x"
data[3] = "x"
data[2] = "o"
data[4] = "o"
data[6] = "o"

print_board ()
