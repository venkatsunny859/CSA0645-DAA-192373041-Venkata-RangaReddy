# EXP61.py - Floyd's Algorithm with Link Failure Simulation

def floyd_algorithm(dist):
    """Floyd-Warshall algorithm"""
    n = len(dist)
    result = [row[:] for row in dist]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                result[i][j] = min(result[i][j], result[i][k] + result[k][j])
    
    return result

print("=" * 70)
print("Floyd's Algorithm with Link Failure Simulation")
print()

# Initial network: 6 routers (0=A, 1=B, 2=C, 3=D, 4=E, 5=F)
routers = ['A', 'B', 'C', 'D', 'E', 'F']
INF = float('inf')

dist_before = [[0, 1, 5, INF, INF, INF],
               [INF, 0, 2, 1, INF, INF],
               [INF, INF, 0, INF, 3, INF],
               [INF, INF, INF, 0, 1, 6],
               [INF, INF, INF, INF, 0, 2],
               [INF, INF, INF, INF, INF, 0]]

print("Before Link Failure:")
print("Distance matrix:")
for row in dist_before:
    print(row)

result_before = floyd_algorithm(dist_before)
print(f"\nShortest path from Router A (0) to Router F (5): {result_before[0][5]}")

# Simulate link failure between B and D (remove edge 1->3)
dist_after = [row[:] for row in dist_before]
dist_after[1][3] = INF

print("\n" + "=" * 70)
print("After Link Failure (B-D link down):")
print("Distance matrix:")
for row in dist_after:
    print(row)

result_after = floyd_algorithm(dist_after)
print(f"\nShortest path from Router A (0) to Router F (5): {result_after[0][5]}")
print("=" * 70)
