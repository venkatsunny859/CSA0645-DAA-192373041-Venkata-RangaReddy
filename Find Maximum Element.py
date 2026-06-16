def find_max(arr):
    max_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num

    return max_val

print(find_max([1,2,3,4,5]))      # 5
print(find_max([7,7,7,7,7]))      # 7
print(find_max([-10,2,3,-4,5]))   # 5