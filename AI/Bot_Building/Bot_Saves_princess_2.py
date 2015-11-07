#!/bin/python
def nextMove(n,r,c,grid):
    xbot = c
    ybot = r
    xprincess = 0
    yprincess = 0
    for i in xrange(0, n):
        row = grid[i]        
        if "p" in row:
            yprincess = i
            xprincess = row.index("p")
    up = yprincess - ybot
    left = xprincess - xbot 
    path = ""
    if up < 0:
        return "UP"
    elif up > 0:
        return "DOWN"
    if left < 0:
        return "LEFT"
    elif left > 0:
        return "RIGHT"

    
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)

