# EXP51.py - Three Assembly Lines with Transfer Times using DP

def three_assembly_lines(lines, transfers):
    """Optimal scheduling for 3 assembly lines"""
    n = len(lines[0])
    dp = [[float('inf')] * n for _ in range(3)]
    
    for i in range(3):
        dp[i][0] = lines[i][0]
    
    for j in range(1, n):
        for i in range(3):
            for k in range(3):
                if i != k:
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + transfers[k][i] + lines[i][j])
                else:
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + lines[i][j])
    
    return min(dp[0][n-1], dp[1][n-1], dp[2][n-1])

print("=" * 60)
print("Three Assembly Lines Problem")
lines = [[5, 9, 3], [6, 8, 4], [7, 6, 5]]
transfers = [[0, 2, 3], [2, 0, 4], [3, 4, 0]]

print(f"Station times:")
print(f"  Line 1: {lines[0]}")
print(f"  Line 2: {lines[1]}")
print(f"  Line 3: {lines[2]}")
print(f"Transfer times: {transfers}")

result = three_assembly_lines(lines, transfers)
print(f"\nMinimum production time: {result}")
print("=" * 60)
