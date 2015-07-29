def solve(N):
    if N%3 == 0:
        return "5"*N
    elif (N-5) >= 0 and (N-5)%3 ==0:
        return "5"*(N-5) + "3"*5
    elif (N-10) >= 0 and (N-10)%3 ==0:
        return "5"*(N-10) + "3"*10
    else:
        return "-1"


T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    print solve(N)
