import math

def binary_search(arr, target):
    """
    Performs a binary search
    - Time complexity: O(log(n))
    - Space complexity: O(1)

    Args:
        arr (list): List of sorted numbers
        target (float): Target to find

    Returns:
        mid (int): Index of the target. Return -1 if not found
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = math.floor((left + right) / 2)
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    arr = [-2,3,4,7,8,9]
    index_target = binary_search(arr, 9)
    if index_target != -1:
        print("Target found at index: {0} with value: {1}".format(index_target, arr[index_target]))
    else:
        print("Target not found")
