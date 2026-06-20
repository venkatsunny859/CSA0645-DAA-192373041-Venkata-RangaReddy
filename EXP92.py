# EXP92.py - Unique Permutations with Duplicates

def unique_permutations(nums):
    """Generate unique permutations with duplicates allowed"""
    nums.sort()
    result = []
    used = [False] * len(nums)
    
    def backtrack(combo):
        if len(combo) == len(nums):
            result.append(combo[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            
            used[i] = True
            combo.append(nums[i])
            backtrack(combo)
            combo.pop()
            used[i] = False
    
    backtrack([])
    return result

print("Unique Permutations with Duplicates")
print()

print("Test 1:")
nums1 = [1, 1, 2]
result1 = unique_permutations(nums1)
print(f"Input: nums = {nums1}")
print(f"Output: {result1}")
print()

print("Test 2:")
nums2 = [1, 2, 3]
result2 = unique_permutations(nums2)
print(f"Input: nums = {nums2}")
print(f"Output: {result2}")
