# Not solved!!
def construct_grid(a):
    grid = [[0 for x in range(len(a))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            grid[i][j] = a[i]^a[j]
    return grid

costlist = []
def F(grid, x, y, cost):
    if x == len(grid)-1 or y == len(grid)-1:
        costlist.append(cost+grid[x][y])
        return cost
    elif grid[x][y] != -1:
        value = grid[x][y]
        grid[x][y] = -1
        if x < len(grid)-1:
            F(grid, x+1, y, cost+value)
        if y < len(grid)-1:
            F(grid, x, y+1, cost+value)
        if x>0: 
            F(grid, x-1, y, cost+value)
        if y>0: 
            F(grid, x, y-1, cost+value)


def minXor(a):
    grid = construct_grid(a)
    for i in range(len(a)):
        F(grid, 0, i, 0)

    return min(costlist)

print minXor([3, 0, 2, 7])


