def insertion_sort(A):
    if len(A) == 1: 
        return A

    for i in range(len(A)):
        value = A[i]
        index = i-1
        while index>=0 and A[index]> value:
            A[index+1] = A[index]
            A[index] = value
            index -=1
    return A



print insertion_sort ([3,4,5,6,1,9,0,8])
