# EXP72.py - Minimum Coins to Add for Target Range

def min_coins_to_add(coins, target):
    """Minimum coins to add to make all values in [1,target] obtainable"""
    coins.sort()
    added = 0
    current_max = 0
    i = 0
    
    while current_max < target:
        if i < len(coins) and coins[i] <= current_max + 1:
            current_max += coins[i]
            i += 1
        else:
            added += 1
            current_max += current_max + 1
    
    return added

print("=" * 70)
print("Minimum Coins to Add for Target Range")
print()

print("Test Case 1:")
coins1 = [1, 4, 10]
target1 = 19
result1 = min_coins_to_add(coins1, target1)
print(f"Input: coins = {coins1}, target = {target1}")
print(f"Output: {result1}")
print("Explanation: Add coins 2 and 8 -> [1,2,4,8,10] covers [1,19]")
print()

print("Test Case 2:")
coins2 = [1, 4, 10, 5, 7, 19]
target2 = 19
result2 = min_coins_to_add(coins2, target2)
print(f"Input: coins = {coins2}, target = {target2}")
print(f"Output: {result2}")
print("Explanation: Add coin 2 -> [1,2,4,5,7,10,19] covers [1,19]")
print("=" * 70)
