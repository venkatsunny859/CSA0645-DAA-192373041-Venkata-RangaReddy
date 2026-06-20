# EXP89.py - Combination Sum

def combination_sum(candidates, target):
    """Find combinations that sum to target"""
    result = []
    
    def backtrack(remaining, combo, start):
        if remaining == 0:
            result.append(combo[:])
            return
        
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            backtrack(remaining - candidates[i], combo, i)
            combo.pop()
    
    backtrack(target, [], 0)
    return result

print("Combination Sum")
print()

print("Test 1:")
cand1 = [2, 3, 6, 7]
target1 = 7
result1 = combination_sum(cand1, target1)
print(f"Input: candidates = {cand1}, target = {target1}")
print(f"Output: {result1}")
print()

print("Test 2:")
cand2 = [2, 3, 5]
target2 = 8
result2 = combination_sum(cand2, target2)
print(f"Input: candidates = {cand2}, target = {target2}")
print(f"Output: {result2}")
