# EXP71.py - Maximize Coins Game (Greedy)

def maximum_coins(piles):
    """Maximize coins by choosing triplets optimally"""
    piles.sort(reverse=True)
    total = 0
    
    for i in range(1, len(piles), 2):
        total += piles[i]
    
    return total

print("=" * 60)
print("Maximize Coins Game")
print()

print("Test Case 1:")
piles1 = [2, 4, 1, 2, 7, 8]
result1 = maximum_coins(piles1[:])
print(f"Input: piles = {piles1}")
print(f"Output: {result1}")
print("Explanation: Choose (2,7,8), you get 7. Choose (1,2,4), you get 2. Total = 9")
print()

print("Test Case 2:")
piles2 = [2, 4, 5]
result2 = maximum_coins(piles2[:])
print(f"Input: piles = {piles2}")
print(f"Output: {result2}")
print("=" * 60)
