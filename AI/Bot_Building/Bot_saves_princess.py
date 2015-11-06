#!/bin/python
def displayPathtoPrincess(n,grid):
    xbot = 0
    ybot = 0
    xprincess = 0
    yprincess = 0
    for i in xrange(0, m):
        row = grid[i]
        if "m" in row:
            ybot = i
            xbot = row.index("m")
        if "p" in row:
            yprincess = i
            xprincess = row.index("p")
    up = yprincess - ybot
    left = xprincess - xbot 
    path = ""
    if up < 0:
        path+="UP\n"*-up
    else:
        path+="DOWN\n"*up
    if left < 0:
        path+="LEFT\n"*-left
    else:
        path+="RIGHT\n"*left

    print path
#print all the moves here
m = input()

grid = []
for i in xrange(0, m):
    row = raw_input().strip()
    grid.append(row)
    
displayPathtoPrincess(m,grid)

