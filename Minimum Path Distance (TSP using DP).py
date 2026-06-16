from functools import lru_cache

def tsp(dist):
    n = len(dist)

    @lru_cache(None)
    def dp(mask, pos):
        if mask == (1 << n) - 1:
            return dist[pos][0]

        ans = float('inf')

        for city in range(n):
            if not (mask & (1 << city)):
                ans = min(ans,
                          dist[pos][city] +
                          dp(mask | (1 << city), city))

        return ans

    return dp(1, 0)

dist = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

print("Minimum Distance =", tsp(dist))