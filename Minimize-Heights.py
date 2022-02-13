# Ques --> https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1


def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[-1] - arr[0]
    small = arr[0] + k
    large = arr[-1] - k
    for i in range(n - 1):
        mn = min(small, arr[i + 1] - k)
        mx = max(large, arr[i] + k)
        if mn < 0: continue
        ans = min(ans, mx - mn)
    return ans


arr = [22, 9, 12, 16, 20]
print(getMinDiff(arr, 5, 3))