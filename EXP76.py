# EXP76.py - Dijkstra's Algorithm (Edge List)

import heapq
from collections import defaultdict

def dijkstra_edge_list(n, edges, source, target):
    """Dijkstra's algorithm using edge list"""
    graph = defaultdict(list)
    
    for u, v, w in edges:
        graph[u].append((v, w))
    
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist[target]

print("=" * 70)
print("Dijkstra's Algorithm (Edge List)")
print()

print("Test Case 1:")
n1 = 6
edges1 = [(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15),
          (2, 3, 11), (2, 5, 2), (3, 4, 6), (4, 5, 9)]
source1, target1 = 0, 4
result1 = dijkstra_edge_list(n1, edges1, source1, target1)
print(f"n = {n1}, edges = {edges1}")
print(f"Shortest path from {source1} to {target1}: {result1}")
print(f"Expected: 20")
print()

print("Test Case 2:")
n2 = 5
edges2 = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9),
          (3, 2, 7), (4, 1, 1), (4, 2, 8), (4, 3, 2)]
source2, target2 = 0, 3
result2 = dijkstra_edge_list(n2, edges2, source2, target2)
print(f"n = {n2}")
print(f"Shortest path from {source2} to {target2}: {result2}")
print(f"Expected: 8")
print("=" * 70)
