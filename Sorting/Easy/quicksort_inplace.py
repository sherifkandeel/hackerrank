def quicksort(A, lo, hi):
  if lo < hi:
    p = partition(A, lo, hi)
    print ' '.join(map(str,A))
    quicksort(A, lo, p - 1)
    quicksort(A, p + 1, hi)


  # lo is the index of the leftmost element of the subarray
  # hi is the index of the rightmost element of the subarray (inclusive)

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, lo, hi):
    pivotIndex = hi 
    pivotValue = A[pivotIndex]
    # put the chosen pivot at A[hi]
    swap(A, pivotIndex, hi)
    #swap A[pivotIndex] and A[hi]
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



m = raw_input()
arr = map(int,raw_input().split(' '))
quicksort(arr, 0, len(arr)-1)

