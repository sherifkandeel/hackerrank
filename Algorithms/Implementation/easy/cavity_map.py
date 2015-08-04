n = int(raw_input())
a = []
for i in xrange(n):
    a.append(list(raw_input()))
aout = a
for i in range(1,n-1):
    for j in range(1,n-1):
        if a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j] and a[i][j]>a[i][j-1] and a[i][j]>a[i][j+1]:
            aout[i][j] = "X"

for m in aout:
    print ''.join(m)
