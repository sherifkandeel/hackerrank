#This is actually cannot be solved by regular permutations, it needs an equation due to the limits being so high
#an equations I came across is that total = M*(M-1)*(M-2)*(M-2)....etc

MOD = 10**9+7

def get_count(m,n):
    total = m
    if n >1:
        total *= (m-1)
    if n> 2:
        total *= pow(m-2,n-2,MOD)
        total %= MOD
    return total%MOD


cases = int(raw_input())
for i in xrange(cases):
    n, m = map(int, raw_input().split(' '))
    total = get_count(m,n)
    print total

