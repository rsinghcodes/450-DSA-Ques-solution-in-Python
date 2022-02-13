# Ques -> Reverse the array

# Time Complexity --> O(1) and Space Complexity --> O(1)

# Without start and end index
# def reverseArray(arr):
#     arr = arr[::-1]

# ------------------------------------------------

# Time Complexity --> O(1) and Space Complexity --> O(1)

# With start and end index
def reverseArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [1,2,3,4]

reverseArray(arr, 0, 3)
print(arr)