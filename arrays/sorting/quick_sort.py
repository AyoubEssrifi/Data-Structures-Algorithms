import numpy as np


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition(arr, start, end):
    pivot = arr[end]
    idx = start

    for i in range(start, end):
        if arr[i] <= pivot:
            swap(arr, i, idx)
            idx += 1

    swap(arr, end, idx)

    return idx

def quicksort(arr, start, end):
    if start >= end:
        return
    idx = partition(arr, start, end)
    quicksort(arr, start, idx - 1)
    quicksort(arr, idx, end)
    
    return arr

if __name__ == '__main__':
    # Testing
    for i in range(100):
        arr = list(np.random.randint(1,100,100))
        sorted_arr = quicksort(arr, 0, len(arr) - 1)
        builtin_sort = sorted(arr)
        if sorted_arr != builtin_sort:
            print("false")
