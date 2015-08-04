def F(wraps, M):
    if wraps < M:
        return 0
    chocs = wraps/M
    wraps = wraps % M + wraps / M
    return chocs+F(wraps, M)


T = int(raw_input())
for i in range (0,T):
    N,C,M = [int(x) for x in raw_input().split(' ')]
    chcolates = 0
    chocolates = N/C
    chocolates += F(chocolates, M)
    print chocolates

