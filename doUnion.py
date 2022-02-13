# Ques -> Given two arrays a[] and b[] of size n and m respectively. The task is to find union (count) between
#         these two arrays.


# Time Complexity --> O(1) and Space Complexity --> O(1)

def doUnion(a, b):
    return len(set(a).union(set(b)))


a = [85, 25, 1, 32, 54, 6]
b = [85, 2]

print(doUnion(a, b))