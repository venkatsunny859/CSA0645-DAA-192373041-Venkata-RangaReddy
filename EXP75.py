# EXP75.py - Dijkstra's Algorithm (Adjacency Matrix)

def dijkstra_matrix(graph, source):
    """Dijkstra's algorithm using adjacency matrix"""
    n = len(graph)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[source] = 0
    
    for _ in range(n):
        min_dist = float('inf')
        u = -1
        
        for v in range(n):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
        
        if u == -1:
            break
        
        visited[u] = True
        
        for v in range(n):
            if not visited[v] and graph[u][v] != float('inf'):
                dist[v] = min(dist[v], dist[u] + graph[u][v])
    
    return dist

print("=" * 70)
print("Dijkstra's Algorithm (Adjacency Matrix)")
print()

INF = float('inf')

print("Test Case 1:")
graph1 = [[0, 10, 3, INF, INF],
          [INF, 0, 1, 2, INF],
          [INF, 4, 0, 8, 2],
          [INF, INF, INF, 0, 7],
          [INF, INF, INF, 9, 0]]
result1 = dijkstra_matrix(graph1, 0)
print(f"Shortest paths from vertex 0: {result1}")
print(f"Expected: [0, 7, 3, 9, 5]")
print()

print("Test Case 2:")
graph2 = [[0, 5, INF, 10],
          [INF, 0, 3, INF],
          [INF, INF, 0, 1],
          [INF, INF, INF, 0]]
result2 = dijkstra_matrix(graph2, 0)
print(f"Shortest paths from vertex 0: {result2}")
print(f"Expected: [0, 5, 8, 9]")
print("=" * 70)
