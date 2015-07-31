def quicksort(A, lo, hi):
  if lo < hi:
    p = partition(A, lo, hi)
    quicksort(A, lo, p - 1)
    quicksort(A, p + 1, hi)


def swap(A, i, j):
    global qsort_swaps
    qsort_swaps +=1
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, lo, hi):
    pivotIndex = hi 
    pivotValue = A[pivotIndex]
    storeIndex = lo
    # Compare remaining array elements against pivotValue = A[hi]
    for i in xrange (lo, hi):
        if A[i] < pivotValue:
            swap(A, i, storeIndex)
            #swap A[i] and A[storeIndex]
            storeIndex = storeIndex + 1
    swap(A,storeIndex, hi)
    #swap A[storeIndex] and A[hi]  # Move pivot to its final place
    return storeIndex


def insertionSort(ar, m):    
    shifts = 0
    for i in xrange(1, m):
        value = ar[i]
        idx = i-1
        while idx>=0 and ar[idx] > value:
            ar[idx+1] = ar[idx]
            shifts +=1
            idx -= 1
        ar[idx+1] = value
    return shifts

def insertionSorting(ar,n):
    arr = [i for i in ar]
    return insertionSort(arr,n)

def quicksorting(ar):
    arr = [i for i in ar]
    quicksort(arr,0, len(arr)-1)


n = int(raw_input())
arr = map(int, raw_input().split(' '))
shifts = insertionSorting(arr, n)
qsort_swaps = 0
quicksorting(arr)
print shifts - qsort_swaps

