rows = int(raw_input())
columns = int(raw_input())
maxcount = 0
grid = [['.'for col in range(columns)] for row in range(rows)]
for i in range(rows):
    grid[i] = map(int, raw_input().split(' '))

def traverse(column, row, count):
    global maxcount
    if grid[row][column] == 1:
        grid[row][column] = 9 # to mark as visited
        count += 1
        #print row,column, count
        if column < len(grid[0])-1:
            count = traverse(column+1, row, count)
        if row < len(grid)-1:
            count = traverse(column,row+1, count)
        if column < len(grid[0])-1 and row > 0:
            count = traverse(column+1 ,row-1, count)
        if column > 0 and row > 0:
            count = traverse(column-1 ,row-1, count)
        if column> 0:
            count = traverse(column-1, row, count)
        if row > 0:
            count = traverse(column, row-1, count)
        if column > 0 and row < len(grid)-1:
            count = traverse(column-1, row+1, count)
        if column< len(grid[0])-1 and row < len(grid)-1:
            count = traverse(column + 1, row + 1, count)
 
    return count
    
totalmax = 0
for i in range(rows):
    for j in range(columns):
        if grid[i][j] == 1:
            maxcount = traverse(j, i, 0)
            if maxcount> totalmax:
                totalmax = maxcount
            maxcount = 0
print totalmax

