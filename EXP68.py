def count_good_pairs(nums):
    
    count = 0
    num_count = {}
    
    for num in nums:
        count += num_count.get(num, 0)
        num_count[num] = num_count.get(num, 0) + 1
    
    return count

print("=" * 60)
print("Count Good Pairs")
print()

print("Test Case 1:")
nums1 = [1, 2, 3, 1, 1, 3]
result1 = count_good_pairs(nums1)
print(f"Input: nums = {nums1}")
print(f"Output: {result1}")
print("Explanation: Pairs (0,3), (0,4), (3,4), (2,5)")
print()

print("Test Case 2:")
nums2 = [1, 1, 1, 1]
result2 = count_good_pairs(nums2)
print(f"Input: nums = {nums2}")
print(f"Output: {result2}")
print("Explanation: All pairs are good (6 pairs total)")
print("=" * 60)
