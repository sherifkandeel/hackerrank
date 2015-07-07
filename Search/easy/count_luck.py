mx = 0
my = 0
grid = []
virgin_grid = []
k = 0


def checkvalidbranch(row, column, grid):
    l = 0
    if column+1 < len(virgin_grid[0]) and (virgin_grid[row][column+1] == '.' or virgin_grid[row][column+1] == '*'):
        l+=1
    if column-1 >= 0 and (virgin_grid[row][column-1] == '.' or virgin_grid[row][column-1] == '*'):
        l+=1
    if row+1 < len(virgin_grid) and (virgin_grid[row+1][column] == '.' or virgin_grid[row+1][column] == '*'):
        l+=1
    if row-1 >= 0 and (virgin_grid[row-1][column] == '.' or virgin_grid[row-1][column] == '*'):
        l+=1
    if row == mx and column == my:
        l+=1
    if l > 2:
        return True
    return False


def traverse(column, row, path, kk):
    if grid[row][column] == '*': #we arrived
        #print path    #if we want to know the right path.
        if kk == k:
            print "Impressed"
        else:
            print "Oops!"
        return 
    elif grid[row][column] == '.':
        grid[row][column] = 'X' #Visited
        if column < len(grid[0])-1:
            if checkvalidbranch(row, column, grid):
                traverse(column+1, row, path +["%d:%d"%(row,column)], kk+1)
            else:
                traverse(column+1, row, path +["%d:%d"%(row,column)], kk)
        if row < len(grid)-1:
            if checkvalidbranch(row, column, grid):
                traverse(column,row+1, path +["%d:%d"%(row,column)], kk+1)
            else:
                traverse(column,row+1, path +["%d:%d"%(row,column)], kk)
        if column> 0:
            if checkvalidbranch(row, column, grid):
                traverse(column-1, row, path +["%d:%d"%(row,column)], kk+1)
            else:
                traverse(column-1, row, path +["%d:%d"%(row,column)], kk)
        if row > 0:
            if checkvalidbranch(row, column, grid):
                traverse(column, row-1, path +["%d:%d"%(row,column)], kk+1)
            else:
                traverse(column, row-1, path +["%d:%d"%(row,column)], kk)


cases = int(raw_input())
for i in range(cases):
    mx = 0
    my = 0
    grid = []
    ksofar = 0
    n,m = map(int, raw_input().split(' '))
    grid = []
    virgin_grid = []
    grid = [['.'for col in range(m)] for row in range(n)]
    virgin_grid = [['.'for col in range(m)] for row in range(n)]
    for j in range(n):
        row = list(raw_input())
        for k in range(m):
            if row[k]=='M':
                mx = j
                my = k
                row[k] = '.'
            grid [j][k] = row[k]
            virgin_grid[j][k] = row[k]
    k = int(raw_input())
    traverse(my, mx, [], 0)
