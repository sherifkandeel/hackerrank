def is_pattern_in_grid(startx, starty, R, grid, pattern):
    counter = 0
    for j in range(startx,R):
        if  pattern[counter] not in grid[j] or (pattern[counter] in grid[j] and grid[j].index(pattern[counter]) != starty):
            return False
        counter +=1
        if counter >= len(pattern):
            break
    return True


def solve(R, C, grid, r, c, pattern):
    starty = -1
    startx = -1
    for i in range(R):
        if pattern[0] in grid[i]:
            starty = grid[i].index(pattern[0])
            startx = i
            if is_pattern_in_grid(startx, starty, R, grid, pattern):
                return "YES"
    return "NO"



T = int(raw_input())
for i in range(T):
    R,C = map(int, raw_input().split(' '))
    grid = []
    for i in range(R):
        grid.append(raw_input())
    r, c = map(int, raw_input().split(' '))
    pattern = []
    for i in range(r):
        pattern.append(raw_input())
    print solve(R, C, grid, r, c, pattern)
