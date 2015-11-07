#!/usr/bin/python
def next_move(posr, posc, board):
        if board[posr][posc] == 'd':
                    print "CLEAN"
    elif 'd' in board[posr][posc:]:
                print "RIGHT"
    elif 'd' in board[posr][:posc]:
                print "LEFT"
    else:
                print "DOWN"
   
    
        
if __name__ == "__main__":
        pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    
    next_move(pos[0], pos[1], board)

