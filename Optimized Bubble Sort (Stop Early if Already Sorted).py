def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop if no swapping occurred
        if not swapped:
            break

    return arr


# Example
arr = [3, 5, 2, 1, 4]
print("Sorted Array:", bubble_sort(arr))