import heapq

def networkDelayTime(times, n, k):

    graph = {}

    for u,v,w in times:
        graph.setdefault(u,[]).append((v,w))

    pq = [(0,k)]

    dist = {i: float('inf') for i in range(1,n+1)}
    dist[k] = 0

    while pq:

        time,node = heapq.heappop(pq)

        if time > dist[node]:
            continue

        for nxt,w in graph.get(node,[]):

            newTime = time + w

            if newTime < dist[nxt]:
                dist[nxt] = newTime
                heapq.heappush(pq,(newTime,nxt))

    ans = max(dist.values())

    return ans if ans != float('inf') else -1