# EXP62.py - Floyd's Algorithm with Distance Threshold

def floyd_algorithm(dist):
    """Floyd-Warshall algorithm"""
    n = len(dist)
    result = [row[:] for row in dist]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                result[i][j] = min(result[i][j], result[i][k] + result[k][j])
    
    return result

def city_with_smallest_neighbors(n, edges, threshold):
    """Find city with smallest neighbors within threshold distance"""
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w
    
    dist = floyd_algorithm(dist)
    
    min_neighbors = float('inf')
    result_city = -1
    
    for i in range(n):
        neighbors = 0
        for j in range(n):
            if i != j and dist[i][j] <= threshold:
                neighbors += 1
        
        if neighbors < min_neighbors:
            min_neighbors = neighbors
            result_city = i
        elif neighbors == min_neighbors and i > result_city:
            result_city = i
    
    return result_city

print("=" * 70)
print("Floyd's Algorithm with Distance Threshold")
print()

print("Test Case 1:")
n1 = 4
edges1 = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
threshold1 = 4
result1 = city_with_smallest_neighbors(n1, edges1, threshold1)
print(f"n = {n1}, edges = {edges1}")
print(f"distanceThreshold = {threshold1}")
print(f"Output: {result1}")
print()

print("Test Case 2:")
n2 = 5
edges2 = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
threshold2 = 2
result2 = city_with_smallest_neighbors(n2, edges2, threshold2)
print(f"n = {n2}, edges = {edges2}")
print(f"distanceThreshold = {threshold2}")
print(f"Output: {result2}")
print("=" * 70)
