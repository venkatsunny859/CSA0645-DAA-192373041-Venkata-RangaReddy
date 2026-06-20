# EXP53.py - TSP with 5 Cities (A, B, C, D, E)

def tsp_5_cities(dist):
    """Find shortest route for 5 cities using DP"""
    n = len(dist)
    memo = {}
    parent = {}
    
    def tsp_dp(mask, pos):
        if mask == (1 << n) - 1:
            return dist[pos][0]
        
        if (mask, pos) in memo:
            return memo[(mask, pos)]
        
        min_cost = float('inf')
        best_next = -1
        
        for next_pos in range(n):
            if not (mask & (1 << next_pos)):
                new_mask = mask | (1 << next_pos)
                cost = dist[pos][next_pos] + tsp_dp(new_mask, next_pos)
                if cost < min_cost:
                    min_cost = cost
                    best_next = next_pos
        
        parent[(mask, pos)] = best_next
        memo[(mask, pos)] = min_cost
        return min_cost
    
    min_dist = tsp_dp(1, 0)
    return min_dist

print("=" * 70)
print("TSP with 5 Cities (A, B, C, D, E)")
print()

cities = ['A', 'B', 'C', 'D', 'E']
dist = [[0, 10, 15, 20, 25],
        [10, 0, 35, 25, 30],
        [15, 35, 0, 30, 20],
        [20, 25, 30, 0, 15],
        [25, 30, 20, 15, 0]]

print("Distance matrix:")
print("   A    B    C    D    E")
for i, city in enumerate(cities):
    print(f"{city}: {dist[i]}")

result = tsp_5_cities(dist)
print(f"\nMinimum total distance for shortest route: {result}")
print("(One possible shortest route: A -> B -> D -> E -> C -> A)")
print("=" * 70)
