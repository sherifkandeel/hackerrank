def quicksort(ar):    
    less = []
    greater = []
    if len(ar) <=1 :
        return ar
    pivot = ar[0]
    for i in ar:
        if i > pivot:
            greater.append(i)
        elif i < pivot:
            less.append(i)
    arr = quicksort(less) + [pivot] + quicksort(greater)
    print ' '.join(map(str,arr))
    return arr


m = input()
ar = [int(i) for i in raw_input().strip().split()]
quicksort(ar)

