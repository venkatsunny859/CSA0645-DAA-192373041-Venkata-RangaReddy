def find_paths(m, n, N, row, col):
    dp = [[0] * n for _ in range(m)]
    dp[row][col] = 1

    count = 0

    for _ in range(N):
        temp = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if dp[r][c]:

                    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = r + dr, c + dc

                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            count += dp[r][c]
                        else:
                            temp[nr][nc] += dp[r][c]

        dp = temp

    return count

print(find_paths(2,2,2,0,0))  # 6
print(find_paths(1,3,3,0,1))  # 12