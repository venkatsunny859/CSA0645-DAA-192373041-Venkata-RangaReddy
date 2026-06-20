# EXP70.py - Network Delay Time (Dijkstra's Algorithm)

import heapq
from collections import defaultdict

def network_delay_time(times, n, k):
    """Find minimum time for signal to reach all nodes"""
    graph = defaultdict(list)
    
    for u, v, w in times:
        graph[u].append((v, w))
    
    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    
    pq = [(0, k)]
    
    while pq:
        d, node = heapq.heappop(pq)
        
        if d > dist[node]:
            continue
        
        for neighbor, time in graph[node]:
            if dist[node] + time < dist[neighbor]:
                dist[neighbor] = dist[node] + time
                heapq.heappush(pq, (dist[neighbor], neighbor))
    
    max_time = max(dist[1:n+1])
    return max_time if max_time != float('inf') else -1

print("=" * 70)
print("Network Delay Time (Dijkstra's Algorithm)")
print()

print("Test Case 1:")
times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n1, k1 = 4, 2
result1 = network_delay_time(times1, n1, k1)
print(f"times = {times1}, n = {n1}, k = {k1}")
print(f"Output: {result1}")
print()

print("Test Case 2:")
times2 = [[1, 2, 1]]
n2, k2 = 2, 1
result2 = network_delay_time(times2, n2, k2)
print(f"times = {times2}, n = {n2}, k = {k2}")
print(f"Output: {result2}")
print()

print("Test Case 3:")
times3 = [[1, 2, 1]]
n3, k3 = 2, 2
result3 = network_delay_time(times3, n3, k3)
print(f"times = {times3}, n = {n3}, k = {k3}")
print(f"Output: {result3}")
print("=" * 70)
