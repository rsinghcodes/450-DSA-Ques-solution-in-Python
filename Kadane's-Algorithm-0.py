def maxSubArraySum(arr, N):
    max_sum = arr[0]
    cur_sum = arr[0]
    for i in range(1, N):
        cur_sum = max(arr[i], cur_sum + arr[i])
        max_sum = max(max_sum, cur_sum)
    return max_sum

arr = [-1,-2,-3,-4]

print(maxSubArraySum(arr, 4))

