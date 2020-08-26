import numpy as np
import math

def selection_sort(arr):
    i = 0
    while i < len(arr):
        j = i
        min = math.inf
        while j < len(arr):
            if arr[j] < min:
                min = arr[j]
                min_idx = j
            j += 1
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
        i += 1
    return arr

for i in range(100):
    arr = list(np.random.randint(1,100,100))
    sorted_arr = selection_sort(arr)
    builtin_sort = sorted(arr)
    if sorted_arr != builtin_sort:
        print("false")
