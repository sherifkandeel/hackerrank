def F(l, summ, arr,output):
    if l == n-1:
        output.add(summ)
        return
    for i in arr:
        F(l+1, summ+i, arr, output)
        


cases = int(raw_input())
for i in xrange(cases):
    n = int(raw_input())
    arr =  []
    #only two test cases
    arr.append(int(raw_input()))
    arr.append(int(raw_input()))

    sout = set()
    F(0,0,arr,sout)

    ss = list(sout)
    ss.sort()
    print ' '.join(map(str,ss))

        

    
