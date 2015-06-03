def F(n,a,b):
    m = n-1
    l = 0
    s_out = set()
    while m>=0:
        s_out.add(l*a + m*b)
        l+=1
        m-=1
    ss = list(s_out)
    ss.sort()
    return ss


cases = int(raw_input())
for i in xrange(cases):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())

    print ' '.join(map(str,F(n,a,b)))

    
