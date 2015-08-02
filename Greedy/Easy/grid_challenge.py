t = int(raw_input())
for i in range(t):
    issorted = True
    n = int(raw_input())
    grid =[]
    for j in range(n):
        row = list(raw_input())
        row.sort()
        grid.append(row)


    for j in range(n):
        col = []
        for k in xrange(1,n):
            if grid[k][j] < grid[k-1][j]:
                issorted = False
                break
    if issorted:
        print "YES"
    else:
        print "NO"

