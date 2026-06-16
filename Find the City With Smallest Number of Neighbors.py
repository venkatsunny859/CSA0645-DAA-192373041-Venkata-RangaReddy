def findCity(n, edges, threshold):

    INF = float('inf')

    dist = [[INF]*n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u,v,w in edges:
        dist[u][v] = w
        dist[v][u] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    city = -1
    minReach = float('inf')

    for i in range(n):
        count = sum(dist[i][j] <= threshold for j in range(n)) - 1

        if count <= minReach:
            minReach = count
            city = i

    return city