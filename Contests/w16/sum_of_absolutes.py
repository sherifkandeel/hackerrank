def solve(a, l, r):
    sum = 0
    for i in range(l-1,r):
        sum=abs(sum + a[i])
    if sum%2 == 0:
        return "Even"
    return "Odd"

n,q = map(int, raw_input().split(' '))
arr = map(int, raw_input().split(' '))
for i in range(q):
    l,r = map(int, raw_input().split(' '))
    print solve(arr, l, r)

