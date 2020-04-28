import copy
import random
# TicTacToe - perfect competitor code outline

# Below, any  variable called "board" contains a board layout string of 9 chars or 'x', 'o' and '_'
# AllBoards is a dictionary of all boards
# key = board, value = the Tboard instance
AllBoards = {}

wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

class Tboard:

    def __init__(self,board,lastmove):
        '''lastmove is the move that led to this board'''
        self.board = board
        self.lastmove = lastmove  # the move (0-8) that led to this board, None if this is the root board

        self.player,self.opponent = WhoseMove(board)

        # state is 'x' if this board is or will be a win for 'x' if the best moves are taken
        # state is 'o' if win for 'o'
        # state is None if we haven't figured this out yet
        self.state = None

        # moves_to_state is how many moves from here to the state if best moves are taken
        # moves_to_state == 0 if this board is actually a final board in the game
        # moves_to_state == None if we haven't figure this out yet
        self.moves_to_state = None

        # best_move is the best next move (0-8) to lead to a win, or if not,
        #   at least a draw, or, sadly, a necessary loss
        #  or -1 if this is a final board
        self.best_move = None

        self.children = [] # list of child Tboards


def FigureItOut(board):
    '''returns a list: best_move, moves_to_state, and state
    best_move (0-8) is, you know, the best move, unless moves_to_state == 0
    if moves_to_state == 0 then we're at the end of the game
    and state is the expected final state: 'x', 'o', or 'd', for X-winning, O-winning, or Draw'''
    AllBoards.clear()

    root = Tboard(board,None)
    AllBoards[board] = root

    # Step 1:
    # Create the board tree starting from this root.
    FindAllBoards(root)

    # Step 2:
    # now traverse the game tree (depth first), filling in best_move, moves_to_state and state
    CalcBestMove(root)

    return [root.best_move, root.moves_to_state, root.state]

def FindAllBoards(board_node):
    ''' Constructs the subtree of boards leading from board_node and puts all such boards (layouts)
    into the dictionary AllBoards.  Uses AllBoards to prevent dublicate boards.  This should
    create a tree of maximum 5478 boards if we start from the empty board.  But usually we won't
    start from the empty board'''

    if board_node in AllBoards:
        return

    AllBoards[board_node.board] = board_node

    # is this a final board?
    endboard = IsEndBoard(board_node.board)  # returns 'x' or 'o' or 'd' if final, else None
    if endboard is not None:   # this board is a win for 'x' or 'o' or a draw
        board_node.state = endboard
        board_node.moves_to_state = 0
        board_node.best_move = -1
        return

    # Now recurse through all the children:
    this_board = board_node.board
    player = board_node.player
    for i in range(9):
        if this_board[i] == '_':
            child_board = this_board[:i]+player+this_board[i+1:]
            child_node = Tboard(child_board,i)
            board_node.children.append(child_node)
            FindAllBoards(child_node)
    return

def next_open (board_node):
    return board_node.board.find ('_')

def remove_nones (dict):
    ans = {}
    for key in dict.keys ():
        if dict[key].state != None:
            ans[key] = dict[key]
    return ans

def bestmove_help (board_node, position, num_moves, dict): #taken from FindAllBoards
    if board_node in dict:
        return

    dict[board_node.board] = board_node

    endboard = IsEndBoard(board_node.board)  # returns 'x' or 'o' or 'd' if final, else None
    if endboard is not None: #and endboard == WhoseMove (board_node.board)[1]:   # this board is a win for 'x' or 'o' or a draw
        board_node.state = endboard
        board_node.moves_to_state = num_moves
        board_node.best_move = position
        return

    # Now recurse through all the children:
    this_board = board_node.board
    player = board_node.player
    for i in range(9):
        if this_board[i] == '_':
            child_board = this_board[:i]+player+this_board[i+1:]
            child_node = Tboard(child_board,i)
            board_node.children.append(child_node)
            bestmove_help(child_node, i, num_moves + 1, dict)
    return

def minimax (board, depth, maximizing_player):
    if depth == 0 or IsEndBoard != None:
        return board.moves_to_state
    if maximizing_player:
        min_moves = float ('inf')
        for child in board.children:
            moves = minimax (child, depth - 1, False)
            min_moves = min (min_moves, moves)
        return min_moves
    else:
        max_moves = float ('-inf')
        for child in board.children:
            moves = minimax (child, depth - 1, True)
            max_moves = max (max_moves, moves)
        return max_moves
def CalcBestMove(board_node):
    '''  updates this board_node with correct values for state, moves_to_state, and best_move
    (This is the engine.)'''

    future_boards = {}
    c = copy.copy (board_node)
    bestmove_help (c, c.lastmove, 0, future_boards)

    #FindAllBoards (board_node)
    #future_boards = remove_nones (future_boards)

    num = 8 #least number of moves to state
    least_moves = [] #list of boards with the least number of moves to state
    for key in future_boards.keys ():
        b = future_boards[key]
        if b.state != None:
            if board_node.board[b.best_move] == '_':
                if b.moves_to_state < num:
                    num = b.moves_to_state
                    least_moves.append (b)
                    for board in least_moves:
                        if board.moves_to_state != num:
                            least_moves.remove (board)
    #print (len (least_moves))
    r = random.randint (0, len (least_moves) - 1)
    node = least_moves[r]
    board_node.state = node.state
    board_node.moves_to_state = node.moves_to_state
    board_node.best_move = node.best_move

    # print ("Board          ", node.board)
    # print ("State          ", board_node.state)
    # print ("Moves to State ", board_node.moves_to_state)
    # print ("Best Move      ", board_node.best_move)

    # print (least_moves[0].board)
    # print (least_moves[1])

def WhoseMove(board):
    '''returns the player (either 'x' or 'o') and also opponent'''
    if board.count('x') == board.count('o'):
        return ['x','o']
    return ['o', 'x']

def IsEndBoard(board):
    for awin in wins:
        if board[awin[0]] != '_' and board[awin[0]] == board[awin[1]] and board[awin[1]] == board[awin[2]]:
            return board[awin[0]]
    if board.count('_') == 0:
        return 'd'
    return None

def PrintBoardNode(node):
    '''for debugging'''
    print('layout',node.board)
    print('last_move',node.lastmove)
    print('player',node.player)
    print('state',node.state)
    print('moves_to_state',node.moves_to_state)
    print('best_move',node.best_move)
    for child_node in node.children:
        print('child',child_node.lastmove,child_node.board)

a = Tboard("_x_______", 1)
CalcBestMove (a)
# print ()
# print ("Best Move      ", a.best_move)
# print ("Moves to State ", a.moves_to_state)


# dict = {}
# bestmove_help (a, 2, 0, dict)
# dict = remove_nones (dict)
# for key in dict.keys():
#     print ("Board          ", key)
#     print ("Moves to State ", dict[key].moves_to_state)
#     print ("State          ", dict[key].state)
#     #print ("Last Move      ", dict[key].last_move)
#     print ("Best Move      ", dict[key].best_move)
#     print ()
