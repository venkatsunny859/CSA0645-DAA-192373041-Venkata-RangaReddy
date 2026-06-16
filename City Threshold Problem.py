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
                dist[i][j] = min(dist[i][j],
                                 dist[i][k]+dist[k][j])

    answer = -1
    minCount = INF

    for city in range(n):
        count = sum(dist[city][j] <= threshold
                    for j in range(n)) - 1

        if count <= minCount:
            minCount = count
            answer = city

    return answer


n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]

print(findCity(n, edges, 4))