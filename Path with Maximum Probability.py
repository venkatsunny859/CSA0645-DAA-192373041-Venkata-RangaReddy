import heapq

def maxProbability(n, edges, succProb, start, end):

    graph = [[] for _ in range(n)]

    for (u,v),p in zip(edges,succProb):
        graph[u].append((v,p))
        graph[v].append((u,p))

    pq = [(-1,start)]

    prob = [0]*n
    prob[start] = 1

    while pq:

        p,node = heapq.heappop(pq)
        p = -p

        if node == end:
            return p

        for nxt,np in graph[node]:

            newProb = p*np

            if newProb > prob[nxt]:
                prob[nxt] = newProb
                heapq.heappush(pq,(-newProb,nxt))

    return 0