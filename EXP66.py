# EXP66.py - Path with Maximum Probability (Modified Dijkstra)

import heapq
from collections import defaultdict

def max_probability(n, edges, probs, start, end):
    """Find path with maximum success probability"""
    graph = defaultdict(list)
    
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, probs[i]))
        graph[v].append((u, probs[i]))
    
    prob = [0.0] * n
    prob[start] = 1.0
    
    pq = [(-1.0, start)]
    
    while pq:
        curr_prob, node = heapq.heappop(pq)
        curr_prob = -curr_prob
        
        if curr_prob < prob[node]:
            continue
        
        for neighbor, edge_prob in graph[node]:
            new_prob = curr_prob * edge_prob
            
            if new_prob > prob[neighbor]:
                prob[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))
    
    return prob[end]

print("=" * 60)
print("Path with Maximum Probability")
print()

print("Test Case 1:")
n1 = 3
edges1 = [[0, 1], [1, 2], [0, 2]]
probs1 = [0.5, 0.5, 0.2]
start1, end1 = 0, 2
result1 = max_probability(n1, edges1, probs1, start1, end1)
print(f"n = {n1}, edges = {edges1}, succProb = {probs1}")
print(f"start = {start1}, end = {end1}")
print(f"Output: {result1:.5f}")
print()

print("Test Case 2:")
n2 = 3
edges2 = [[0, 1], [1, 2], [0, 2]]
probs2 = [0.5, 0.5, 0.3]
start2, end2 = 0, 2
result2 = max_probability(n2, edges2, probs2, start2, end2)
print(f"n = {n2}, edges = {edges2}, succProb = {probs2}")
print(f"start = {start2}, end = {end2}")
print(f"Output: {result2:.5f}")
print("=" * 60)
