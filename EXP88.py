# EXP88.py - Sum of Subarray Minimums

def sum_subarray_mins(arr):
    """Sum of minimums across all subarrays"""
    MOD = 10**9 + 7
    n = len(arr)
    total = 0
    
    for i in range(n):
        min_val = arr[i]
        for j in range(i, n):
            min_val = min(min_val, arr[j])
            total = (total + min_val) % MOD
    
    return total

print("Sum of Subarray Minimums")
print()

print("Test 1:")
arr1 = [3, 1, 2, 4]
result1 = sum_subarray_mins(arr1)
print(f"Input: arr = {arr1}")
print(f"Output: {result1}")
print("Explanation: [3]=3, [1]=1, [2]=2, [4]=4, [3,1]=1, [1,2]=1, [2,4]=2, [3,1,2]=1, [1,2,4]=1, [3,1,2,4]=1")
print()

print("Test 2:")
arr2 = [11, 81, 94, 43, 3]
result2 = sum_subarray_mins(arr2)
print(f"Input: arr = {arr2}")
print(f"Output: {result2}")
