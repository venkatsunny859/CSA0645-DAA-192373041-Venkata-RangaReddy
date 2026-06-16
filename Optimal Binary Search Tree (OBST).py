def optimal_bst(freq):
    n = len(freq)

    cost = [[0]*(n+1) for _ in range(n+1)]
    root = [[0]*(n+1) for _ in range(n+1)]

    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + freq[i]

    for length in range(1, n+1):
        for i in range(n-length+1):
            j = i + length

            cost[i][j] = float('inf')
            total = prefix[j] - prefix[i]

            for r in range(i, j):
                c = cost[i][r] + cost[r+1][j] + total

                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root

keys = [10,12,16,21]
freq = [4,2,6,3]

cost, root = optimal_bst(freq)

print("Optimal Cost =", int(cost[0][4]))