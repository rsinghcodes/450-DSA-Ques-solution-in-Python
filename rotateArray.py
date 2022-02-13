# Ques -> Cyclically rotate an array

# Time Complexity --> O(1) and Space Complexity --> O(1)

def rotateArray(arr, d):
    arr = arr[-d:] + arr[:-d]
    return arr

arr = [1, 2, 3, 4, 5]
d = 3
print(rotateArray(arr,d))