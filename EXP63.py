# EXP63.py - Optimal Binary Search Tree (OBST)

def optimal_bst(freq):
    """Calculate OBST cost and root"""
    n = len(freq)
    cost = [[0] * (n + 1) for _ in range(n + 2)]
    root = [[0] * n for _ in range(n)]
    
    for i in range(n):
        cost[i + 1][i] = 0
        cost[i + 1][i + 1] = freq[i]
    
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            cost[i][j - 1] = float('inf')
            
            for r in range(i, j + 1):
                left_cost = cost[i][r - 1]
                right_cost = cost[r + 1][j]
                sum_freq = sum(freq[r - 1:j])
                total = left_cost + right_cost + sum_freq
                
                if total < cost[i][j]:
                    cost[i][j] = total
                    root[i - 1][j - 1] = r - 1
    
    return cost[1][n], cost, root

print("=" * 60)
print("Optimal Binary Search Tree (OBST)")
print()

print("Test Case 1:")
freq1 = [0.1, 0.2, 0.4, 0.3]
keys1 = ['A', 'B', 'C', 'D']
min_cost1, cost1, root1 = optimal_bst(freq1)
print(f"Keys: {keys1}")
print(f"Frequencies: {freq1}")
print(f"Minimum Cost: {min_cost1}")
print()

print("Test Case 2:")
freq2 = [34, 8, 50]
min_cost2, cost2, root2 = optimal_bst(freq2)
print(f"Frequencies: {freq2}")
print(f"Minimum Cost: {min_cost2}")
print()

print("Test Case 3:")
freq3 = [4, 2, 6, 3]
min_cost3, cost3, root3 = optimal_bst(freq3)
print(f"Frequencies: {freq3}")
print(f"Minimum Cost: {min_cost3}")
print("=" * 60)
