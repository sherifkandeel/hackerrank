from random import shuffle
import random
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def linear_search(arr, number):
    for i in arr:
        if i == number:
            return True
    return False

def binary_search(arr, s, f, number):
    if s>=f:
        return False
    mid = (s+f)/2
    if arr[mid] == number:
        return True
    if number >= arr[mid]:
        return binary_search(arr, mid+1, f, number)
    else:
        return binary_search(arr, s, mid, number)

print binary_search(arr, 0, len(arr), 3)




def selection_sort(arr):
    for i in range(len(arr)):
        minidx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minidx]:
                minidx = j
        temp = arr[i]
        arr[i] = arr[minidx]
        arr[minidx] = temp


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]: 
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp





shuffle(arr)
print arr
# selection_sort(arr)
bubble_sort(arr)
print arr





