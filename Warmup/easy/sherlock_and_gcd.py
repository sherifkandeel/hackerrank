def divisor_exists(a):
    m = min(a)
    if m==1:
        return False 
    for i in xrange(2,m+1):
        flag = 0
        for j in a:
            if j%i != 0:
                flag = 1
        if flag == 0:
            return True
    return False


def repitition_exists(a):
    n = len(a)
    if len(set(a))<n:
        return True
    return False


def solve(n, a):
    if n<=1: return "NO"
    for ws in xrange(2,n+1):
        for i in xrange(0,n-ws+1):
            aa = a[i:i+ws]
            if repitition_exists(aa):
                continue
            elif divisor_exists(aa):
                continue
            print aa
            return "YES"
    return "NO"    


T = int(raw_input())
for i in xrange(T):
    n = int(raw_input())
    a = map(int, raw_input().split(' '))
    print solve(n,a)

