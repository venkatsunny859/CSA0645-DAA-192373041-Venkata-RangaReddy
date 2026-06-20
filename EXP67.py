# EXP67.py - Unique Paths in Grid (DP)

def unique_paths(m, n):
    """Count unique paths from top-left to bottom-right"""
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]

print("=" * 60)
print("Unique Paths in Grid (Robot Movement)")
print()

print("Test Case 1:")
m1, n1 = 3, 7
result1 = unique_paths(m1, n1)
print(f"Input: m = {m1}, n = {n1}")
print(f"Output: {result1}")
print()

print("Test Case 2:")
m2, n2 = 3, 2
result2 = unique_paths(m2, n2)
print(f"Input: m = {m2}, n = {n2}")
print(f"Output: {result2}")
print("Explanation: 3 ways to reach bottom-right:")
print("  1. Right -> Down -> Down")
print("  2. Down -> Down -> Right")
print("  3. Down -> Right -> Down")
print("=" * 60)
