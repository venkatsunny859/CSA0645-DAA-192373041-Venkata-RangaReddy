def binary_search(arr, key):
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [3,4,6,-9,10,8,9,30]

result = binary_search(arr, 10)

if result != -1:
    print("Element 10 found at position", result + 1)
else:
    print("Element not found")