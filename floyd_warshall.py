INF = float('inf')

routers = [
[0,1,5,INF,INF,INF],
[1,0,2,1,INF,INF],
[5,2,0,INF,3,INF],
[INF,1,INF,0,1,6],
[INF,INF,3,1,0,2],
[INF,INF,INF,6,2,0]
]

before = floyd_warshall(routers)

print("A to F Before Failure =", before[0][5])

routers[1][3] = INF
routers[3][1] = INF

after = floyd_warshall(routers)

print("A to F After Failure =", after[0][5])