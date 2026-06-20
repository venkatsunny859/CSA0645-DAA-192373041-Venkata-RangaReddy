def count_dice_ways(num_sides, num_dice, target):
    """Count ways to get target sum using DP"""
    dp = [[0] * (target + 1) for _ in range(num_dice + 1)]
    dp[0][0] = 1
    
    for i in range(1, num_dice + 1):
        for j in range(i, min(target + 1, i * num_sides + 1)):
            for k in range(1, num_sides + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
    
    return dp[num_dice][target]

print("=" * 50)
print("Test Case 1:")
print("Number of sides: 6, Number of dice: 2, Target: 7")
result1 = count_dice_ways(6, 2, 7)
print(f"Output: Number of ways = {result1}")
print()

print("Test Case 2:")
print("Number of sides: 4, Number of dice: 3, Target: 10")
result2 = count_dice_ways(4, 3, 10)
print(f"Output: Number of ways = {result2}")
print("=" * 50)
