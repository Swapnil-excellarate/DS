def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = abs(arr[1] - arr[0])
    for i in range(len(arr) - 1):
        diff = abs(arr[i + 1] - arr[i])
        if diff < min_diff:
            min_diff = diff
    return min_diff

arr=[1,31,5,10,115]
print(minimumAbsoluteDifference(arr))
