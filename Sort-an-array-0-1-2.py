# Ques -> Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

# Time Complexity --> O(1) and Space Complexity --> O(1)

def sort012(arr, n):
    arr.sort()
    return arr

arr = [0, 2, 1, 2, 0]
print(sort012(arr, 5))