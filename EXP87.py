# EXP87.py - Target Sum with Symbols

def find_target_ways(nums, target):
    """Count expressions with +/- that evaluate to target"""
    def backtrack(index, current_sum):
        if index == len(nums):
            return 1 if current_sum == target else 0
        
        pos_ways = backtrack(index + 1, current_sum + nums[index])
        neg_ways = backtrack(index + 1, current_sum - nums[index])
        
        return pos_ways + neg_ways
    
    return backtrack(0, 0)

print("Target Sum Problem")
print()

print("Test 1:")
nums1 = [1, 1, 1, 1, 1]
target1 = 3
result1 = find_target_ways(nums1, target1)
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {result1}")
print()

print("Test 2:")
nums2 = [1]
target2 = 1
result2 = find_target_ways(nums2, target2)
print(f"Input: nums = {nums2}, target = {target2}")
print(f"Output: {result2}")
