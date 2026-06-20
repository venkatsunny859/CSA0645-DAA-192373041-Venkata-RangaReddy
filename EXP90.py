# EXP90.py - Combination Sum 2 (Each element used once)

def combination_sum2(candidates, target):
    """Find unique combinations that sum to target (each element used once)"""
    candidates.sort()
    result = []
    
    def backtrack(remaining, combo, start):
        if remaining == 0:
            result.append(combo[:])
            return
        
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            
            combo.append(candidates[i])
            backtrack(remaining - candidates[i], combo, i + 1)
            combo.pop()
    
    backtrack(target, [], 0)
    return result

print("Combination Sum 2")
print()

print("Test 1:")
cand1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8
result1 = combination_sum2(cand1, target1)
print(f"Input: candidates = {cand1}, target = {target1}")
print(f"Output: {result1}")
print()

print("Test 2:")
cand2 = [2, 5, 2, 1, 2]
target2 = 5
result2 = combination_sum2(cand2, target2)
print(f"Input: candidates = {cand2}, target = {target2}")
print(f"Output: {result2}")
