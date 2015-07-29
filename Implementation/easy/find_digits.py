cases = int(raw_input())
for i in xrange(cases):
    n = int(raw_input())
    count = 0 
    m =n
    while n!= 0:
        div = n%10
        if div !=0 and m % div == 0:
            count += 1
        n /=10
    print count


