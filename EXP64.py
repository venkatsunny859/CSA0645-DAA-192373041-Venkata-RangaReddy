# EXP64.py - OBST with Frequencies

def optimal_bst_with_display(keys, freq):
    """OBST with cost and root matrices display"""
    n = len(keys)
    cost = [[0] * (n + 1) for _ in range(n + 2)]
    root = [[0] * n for _ in range(n)]
    
    for i in range(n):
        cost[i + 1][i + 1] = freq[i]
    
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            cost[i][j] = float('inf')
            
            for r in range(i, j + 1):
                sum_freq = sum(freq[r - 1:j])
                total = cost[i][r - 1] + cost[r + 1][j] + sum_freq
                
                if total < cost[i][j]:
                    cost[i][j] = total
                    root[i - 1][j - 1] = r
    
    return cost[1][n], cost, root

print("=" * 70)
print("Optimal Binary Search Tree with Frequencies")
print()

print("Test Case 1:")
keys1 = [10, 12]
freq1 = [34, 50]
min_cost1, cost1, root1 = optimal_bst_with_display(keys1, freq1)
print(f"Keys: {keys1}, Frequencies: {freq1}")
print(f"Output: {min_cost1}")
print()

print("Test Case 2:")
keys2 = [10, 12, 16, 21]
freq2 = [4, 2, 6, 3]
min_cost2, cost2, root2 = optimal_bst_with_display(keys2, freq2)
print(f"Keys: {keys2}, Frequencies: {freq2}")
print(f"Output: {min_cost2}")
print()

print("Test Case 3:")
keys3 = [10, 12, 20]
freq3 = [34, 8, 50]
min_cost3, cost3, root3 = optimal_bst_with_display(keys3, freq3)
print(f"Keys: {keys3}, Frequencies: {freq3}")
print(f"Output: {min_cost3}")
print("=" * 70)
