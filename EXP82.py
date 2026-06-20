# EXP82.py - MST Uniqueness Verification

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
    """Find MST using Kruskal's algorithm"""
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
    
    return mst_edges, total_weight

def is_mst_unique(n, edges, given_mst):
    """Check if given MST is unique"""
    mst_edges, mst_weight = kruskal_mst(n, edges)
    given_weight = sum(w for _, _, w in given_mst)
    
    if given_weight != mst_weight:
        return False
    
    given_set = set((min(u, v), max(u, v), w) for u, v, w in given_mst)
    mst_set = set((min(u, v), max(u, v), w) for u, v, w in mst_edges)
    
    if given_set == mst_set:
        return True
    
    for u, v, w in mst_edges:
        if (min(u, v), max(u, v), w) not in given_set:
            if sum(1 for a, b, c in edges if c == w and (min(a,b), max(a,b)) != (min(u,v), max(u,v))) > 0:
                return False
    
    return True

print("=" * 70)
print("MST Uniqueness Verification")
print()

print("Test Case 1:")
n1 = 4
edges1 = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
given_mst1 = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
unique1 = is_mst_unique(n1, edges1, given_mst1)
print(f"Given MST: {given_mst1}")
print(f"Is unique? {unique1}")
print()

print("Test Case 2:")
n2 = 5
edges2 = [(0, 1, 1), (0, 2, 1), (1, 3, 2), (2, 3, 2), (3, 4, 3), (4, 2, 3)]
given_mst2 = [(0, 1, 1), (0, 2, 1), (1, 3, 2), (3, 4, 3)]
unique2 = is_mst_unique(n2, edges2, given_mst2)
print(f"Given MST: {given_mst2}")
print(f"Is unique? {unique2}")
print(f"Alternative MST: [(0,1,1), (0,2,1), (2,3,2), (3,4,3)]")
print("=" * 70)
