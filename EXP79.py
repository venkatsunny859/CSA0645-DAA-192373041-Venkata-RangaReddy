# EXP79.py - Greedy Container Loading (Maximum Weight)

def max_container_weight(weights, max_capacity):
    """Maximum weight that can fit in container (greedy - heavy items first)"""
    weights.sort(reverse=True)
    total_weight = 0
    
    for weight in weights:
        if total_weight + weight <= max_capacity:
            total_weight += weight
    
    return total_weight

print("=" * 70)
print("Greedy Container Loading - Maximum Weight")
print()

print("Test Case 1:")
weights1 = [10, 20, 30, 40, 50]
capacity1 = 60
result1 = max_container_weight(weights1, capacity1)
print(f"Weights: {weights1}")
print(f"Max capacity: {capacity1}")
print(f"Output: {result1}")
print("Explanation: Pick 50, then can't fit 40. Total = 50")
print()

print("Test Case 2:")
weights2 = [5, 10, 15, 20, 25, 30]
capacity2 = 50
result2 = max_container_weight(weights2, capacity2)
print(f"Weights: {weights2}")
print(f"Max capacity: {capacity2}")
print(f"Output: {result2}")
print("Explanation: Pick 30, then 20. Total = 50")
print("=" * 70)
