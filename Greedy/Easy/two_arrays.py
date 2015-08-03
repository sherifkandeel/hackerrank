def solve(a1, a2, k, n):
    a1.sort()
    a2.sort(reverse=True)
    for i in range(n):
        if a1[i]+a2[i] < k:
            return "NO"
    return "YES"

t = int(raw_input())
for i in range(t):
    n, k = map(int, raw_input().split(' '))
    a1 = map(int, raw_input().split(' '))
    a2 = map(int, raw_input().split(' '))
    print solve(a1, a2, k, n)
