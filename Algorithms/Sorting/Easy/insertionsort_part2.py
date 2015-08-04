def insertionSort(ar, m):    
    for i in xrange(1, m):
        value = ar[i]
        idx = i-1
        while idx>=0 and ar[idx] > value:
            ar[idx+1] = ar[idx]
            shifts +=1
            idx -= 1
        ar[idx+1] = value
        print ' '.join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar, m)

