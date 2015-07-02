def solve(A):
    summ = 0
    for i in A:
        summ += i
    left = 0
    right = summ
    for i in A:
        right-=i
        if left == right:
            return "YES"
        left+=i
    return "NO"
        

cases = int(raw_input())
for i in range(cases):
    n = int(raw_input())
    A = map(int, raw_input().split(' '))
    print solve(A)

