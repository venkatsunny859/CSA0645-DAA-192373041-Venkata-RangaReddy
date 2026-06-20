# EXP69.py - City with Smallest Number of Neighbors at Distance Threshold

def find_the_city(n, edges, distance_threshold):
    """Find city with smallest neighbors within distance threshold"""
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    min_count = float('inf')
    result_city = -1
    
    for i in range(n):
        count = 0
        for j in range(n):
            if dist[i][j] <= distance_threshold:
                count += 1
        
        if count < min_count or (count == min_count and i > result_city):
            min_count = count
            result_city = i
    
    return result_city

print("=" * 70)
print("City with Smallest Number of Neighbors at Distance Threshold")
print()

print("Test Case 1:")
n1 = 4
edges1 = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
threshold1 = 4
result1 = find_the_city(n1, edges1, threshold1)
print(f"n = {n1}, edges = {edges1}")
print(f"distanceThreshold = {threshold1}")
print(f"Output: {result1}")
print()

print("Test Case 2:")
n2 = 5
edges2 = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
threshold2 = 2
result2 = find_the_city(n2, edges2, threshold2)
print(f"n = {n2}, edges = {edges2}")
print(f"distanceThreshold = {threshold2}")
print(f"Output: {result2}")
print("=" * 70)
