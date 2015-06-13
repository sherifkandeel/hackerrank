def insertionSort(ar, m):    
    value = ar[m-1]
    i = m-2
    while i>=0 and ar[i]>value:
        ar[i+1] = ar[i]
        i -=1
        print str(ar).replace('[','').replace(']','').replace(',','')
    ar[i+1] = value
    print str(ar).replace('[','').replace(']','').replace(',','')

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar, m)

