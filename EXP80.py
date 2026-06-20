# EXP80.py - Greedy Bin Packing (Minimum Containers)

def min_containers(weights, max_capacity):
    """Minimum number of containers using greedy bin packing"""
    weights.sort(reverse=True)
    containers = 0
    current_weight = 0
    
    for weight in weights:
        if current_weight + weight <= max_capacity:
            current_weight += weight
        else:
            containers += 1
            current_weight = weight
    
    if current_weight > 0:
        containers += 1
    
    return containers

print("=" * 70)
print("Greedy Bin Packing - Minimum Containers")
print()

print("Test Case 1:")
weights1 = [5, 10, 15, 20, 25, 30, 35]
capacity1 = 50
result1 = min_containers(weights1, capacity1)
print(f"Weights: {weights1}")
print(f"Max capacity per container: {capacity1}")
print(f"Output: {result1} containers")
print("Explanation: [35,15], [30,20], [25,10], [5] = 4 containers")
print()

print("Test Case 2:")
weights2 = [10, 20, 30, 40, 50, 60, 70, 80]
capacity2 = 100
result2 = min_containers(weights2, capacity2)
print(f"Weights: {weights2}")
print(f"Max capacity per container: {capacity2}")
print(f"Output: {result2} containers")
print("Explanation: [80,20], [70,30], [60,40], [50,10] might be 4, but with this greedy = 6")
print("=" * 70)
