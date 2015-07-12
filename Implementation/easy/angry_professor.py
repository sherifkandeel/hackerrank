cases = int (raw_input())
for i in xrange(cases):
    n,k = map(int,raw_input().split(' '))
    times = map(int, raw_input().split(' '))
    for time in times: 
        if time <= 0:
            k-=1
            if k==0:
                print "NO"
    if k>0:
        print "YES"                
