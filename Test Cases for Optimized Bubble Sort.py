def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# Test Case 1
print(bubble_sort([64, 25, 12, 22, 11]))

# Test Case 2
print(bubble_sort([29, 10, 14, 37, 13]))

# Test Case 3
print(bubble_sort([3, 5, 2, 1, 4]))

# Test Case 4 (Already Sorted)
print(bubble_sort([1, 2, 3, 4, 5]))

# Test Case 5 (Reverse Sorted)
print(bubble_sort([5, 4, 3, 2, 1]))