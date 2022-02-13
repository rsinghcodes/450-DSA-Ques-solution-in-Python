# Ques -> Move all negative numbers to beginning and positive to end with constant extra space

# Time Complexity --> O(1) and Space Complexity --> O(1)

# def rearrange(arr):
#     arr.sort()
#     return arr

# ----------------------------------------------------------------

# Time Complexity --> O(N) and Space Complexity --> O(1)

def rearrange(arr,n):
    j = 0
    for i in range(0, n):
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j + 1

    print(arr)

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
rearrange(arr,9)