# Ques -> Given an array arr[] and an integer K where K is smaller than size of array,
# the task is to find the Kth smallest element in the given array.
# It is given that all array elements are distinct.

def kthSmallest(arr, l, r,k):
    arr.sort()
    return arr[k-1]

arr = [7, 10, 4, 3, 20, 15]

print(kthSmallest(arr, 0, 5, 3))