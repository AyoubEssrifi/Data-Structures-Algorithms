import numpy as np

def bubble_sort(arr):
    j = len(arr) - 1
    while j >= 0:
        i = 0
        while i < j:
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            i += 1
        j -= 1
    return arr

# Testing
for i in range(100):
    arr = list(np.random.randint(1,100,100))
    sorted_arr = bubble_sort(arr)
    builtin_sort = sorted(arr)
    if sorted_arr != builtin_sort:
        print("false")