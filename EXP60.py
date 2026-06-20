# EXP60.py - Floyd's Algorithm for Shortest Path

def floyd_algorithm(dist):
    """Floyd-Warshall algorithm for all-pairs shortest path"""
    n = len(dist)
    result = [row[:] for row in dist]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                result[i][j] = min(result[i][j], result[i][k] + result[k][j])
    
    return result

print("=" * 70)
print("Floyd's Algorithm - Shortest Path Between All Pairs")
print()

print("Test Case 1:")
dist1 = [[0, 3, float('inf'), float('inf')],
         [float('inf'), 0, 1, float('inf')],
         [float('inf'), float('inf'), 0, 1],
         [float('inf'), 4, float('inf'), 0]]

print("Initial Distance Matrix:")
for row in dist1:
    print(row)

result1 = floyd_algorithm(dist1)
print("\nAfter Floyd's Algorithm:")
for row in result1:
    print(row)

print(f"\nShortest path from City 0 to City 3: {result1[0][3]}")
print()

print("Test Case 2 (With Negative Edges):")
dist2 = [[0, 3, 8, float('inf')],
         [float('inf'), 0, 4, 1],
         [2, float('inf'), 0, -5],
         [float('inf'), 6, float('inf'), 0]]

print("Initial Distance Matrix:")
for row in dist2:
    print(row)

result2 = floyd_algorithm(dist2)
print("\nAfter Floyd's Algorithm:")
for row in result2:
    print(row)

print(f"\nShortest path from City 0 to City 2: {result2[0][2]}")
print("=" * 70)
