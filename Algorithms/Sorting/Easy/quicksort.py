def quicksort(arr):
    less = []
    greater = []
    equal = []
    if len(arr) > 1:
        pivot = arr[0]
        for i in arr:
            if i > pivot:
                greater.append(i)
            elif i < pivot:
                less.append(i)
            else:
                equal.append(i)
        array = quicksort(less)+equal+quicksort(greater)
        print array
        return array
    else:
        return arr




def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


array=[12,12,4,5,6,7,3,1,15]
array2=[5,8,1,3,7,9,2]
arr = [1,0]
quicksort(array2)
