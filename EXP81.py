# EXP81.py - Kruskal's Algorithm (Minimum Spanning Tree)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal_mst(n, edges):
    """Kruskal's algorithm for MST"""
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            if len(mst_edges) == n - 1:
                break
    
    return mst_edges, total_weight

print("=" * 70)
print("Kruskal's Algorithm - Minimum Spanning Tree")
print()

print("Test Case 1:")
n1 = 4
edges1 = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
mst1, weight1 = kruskal_mst(n1, edges1)
print(f"n = {n1}, m = {len(edges1)}")
print(f"Edges: {edges1}")
print(f"MST Edges: {mst1}")
print(f"Total weight: {weight1}")
print(f"Expected: 19")
print()

print("Test Case 2:")
n2 = 5
edges2 = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
mst2, weight2 = kruskal_mst(n2, edges2)
print(f"n = {n2}, m = {len(edges2)}")
print(f"MST Edges: {mst2}")
print(f"Total weight: {weight2}")
print(f"Expected: 16")
print("=" * 70)
