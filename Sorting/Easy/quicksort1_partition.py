def partition(ar):    
    less = []
    greater = []
    pivot = ar[0]
    for i in ar:
        if i > pivot:
            greater.append(i)
        elif i < pivot:
            less.append(i)
    return ' '.join(map(str, less + [pivot] + greater))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print partition(ar)

