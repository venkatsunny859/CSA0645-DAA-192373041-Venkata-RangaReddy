# EXP93.py - Graph Coloring

def graph_coloring(n, edges, k):
    """Graph coloring with k colors"""
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1] * n
    
    def is_safe(node, c):
        for neighbor in graph[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for c in range(k):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1
        
        return False
    
    if backtrack(0):
        return color
    return None

print("Graph Coloring Problem")
print()

n = 4
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
k = 3

result = graph_coloring(n, edges, k)
print(f"n = {n}, edges = {edges}, k = {k}")
print(f"Coloring: {result}")
print(f"Colors used: {len(set(c for c in result if c != -1))}")
