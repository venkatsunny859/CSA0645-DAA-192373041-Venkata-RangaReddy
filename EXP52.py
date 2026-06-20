# EXP52.py - Traveling Salesman Problem - Minimum Path using DP (Held-Karp)

def tsp_held_karp(dist):
    """TSP using Held-Karp algorithm (DP with bitmask)"""
    n = len(dist)
    memo = {}
    
    def tsp_dp(mask, pos):
        if mask == (1 << n) - 1:
            return dist[pos][0]
        
        if (mask, pos) in memo:
            return memo[(mask, pos)]
        
        min_cost = float('inf')
        for next_pos in range(n):
            if not (mask & (1 << next_pos)):
                new_mask = mask | (1 << next_pos)
                cost = dist[pos][next_pos] + tsp_dp(new_mask, next_pos)
                min_cost = min(min_cost, cost)
        
        memo[(mask, pos)] = min_cost
        return min_cost
    
    return tsp_dp(1, 0)

print("=" * 60)
print("Traveling Salesman Problem - Minimum Path")
print()

print("Test Case 1:")
dist1 = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]
result1 = tsp_held_karp(dist1)
print(f"Distance matrix:\n{dist1}")
print(f"Output: Minimum distance = {result1}")
print()

print("Test Case 2:")
dist2 = [[0, 10, 10, 10],
         [10, 0, 10, 10],
         [10, 10, 0, 10],
         [10, 10, 10, 0]]
result2 = tsp_held_karp(dist2)
print(f"Output: Minimum distance = {result2}")
print()

print("Test Case 3:")
dist3 = [[0, 1, 2, 3],
         [1, 0, 4, 5],
         [2, 4, 0, 6],
         [3, 5, 6, 0]]
result3 = tsp_held_karp(dist3)
print(f"Output: Minimum distance = {result3}")
print("=" * 60)
