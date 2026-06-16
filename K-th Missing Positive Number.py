def find_kth_positive(arr, k):

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        missing = arr[mid] - (mid + 1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    return left + k


print(find_kth_positive([2, 3, 4, 7, 11], 5))
print(find_kth_positive([1, 2, 3, 4], 2))