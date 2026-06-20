# EXP91.py - Permutations

def permutations(nums):
    """Generate all permutations of nums"""
    result = []
    
    def backtrack(combo):
        if len(combo) == len(nums):
            result.append(combo[:])
            return
        
        for num in nums:
            if num not in combo:
                combo.append(num)
                backtrack(combo)
                combo.pop()
    
    backtrack([])
    return result

print("Permutations")
print()

print("Test 1:")
nums1 = [1, 2, 3]
result1 = permutations(nums1)
print(f"Input: nums = {nums1}")
print(f"Output: {result1}")
print()

print("Test 2:")
nums2 = [0, 1]
result2 = permutations(nums2)
print(f"Input: nums = {nums2}")
print(f"Output: {result2}")
print()

print("Test 3:")
nums3 = [1]
result3 = permutations(nums3)
print(f"Input: nums = {nums3}")
print(f"Output: {result3}")
