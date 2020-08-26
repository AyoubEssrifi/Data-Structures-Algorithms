import numpy as np

def insertion_sort(arr):
    """
    Performs an insertion sorting algorithm
    - Time complexity: O(n²)
    - Space complexity: O(n)

    Args:
        arr (list): List to sort

    Returns:
        (list): Sorted list
    """
    i = 1
    while i < len(arr):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
            else: 
                break
            j -= 1
        i += 1
    return arr

# Testing 
for i in range(100):
    arr = list(np.random.randint(1, 100, 50))
    sorted_arr = insertion_sort(arr)
    inbuilt_sort = sorted(arr)

    if sorted_arr != inbuilt_sort:
        print("false")
        break