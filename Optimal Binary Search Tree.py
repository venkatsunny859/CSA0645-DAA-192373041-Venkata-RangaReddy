def obst(freq):

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
                    root[i][j] = r + 1

    return cost, root


freq = [0.1,0.2,0.4,0.3]

cost, root = obst(freq)

print("Optimal Cost =", cost[0][4])