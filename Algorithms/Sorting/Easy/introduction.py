v = int(raw_input())
n = int(raw_input())
A = map(int, raw_input().split(' '))

for i in xrange(n):
    if A[i] == v:
        print i
        break
