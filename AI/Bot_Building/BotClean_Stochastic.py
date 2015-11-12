#!/usr/bin/python
def nextMove(posr, posc, board):
    if board[posr][posc] == 'd':
        print "CLEAN"
        return
    elif 'd' in board[posr][posc:]:
        print "RIGHT"
        return
    elif 'd' in board[posr][:posc]:
        print "LEFT"
        return
        
    for i in range(len(board)):
        if 'd' in board[i]:
            if i <posr:
                print "UP"
            else:
                print "DOWN"
            return
    
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)

