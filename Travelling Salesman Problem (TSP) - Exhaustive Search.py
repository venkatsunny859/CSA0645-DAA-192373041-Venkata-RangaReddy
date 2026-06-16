import math
from itertools import permutations

def distance(city1, city2):
    return math.sqrt(
        (city1[0] - city2[0])**2 +
        (city1[1] - city2[1])**2
    )

def tsp(cities):

    start = cities[0]
    min_distance = float('inf')
    best_path = None

    for perm in permutations(cities[1:]):

        path = [start] + list(perm) + [start]

        total = 0

        for i in range(len(path)-1):
            total += distance(path[i], path[i+1])

        if total < min_distance:
            min_distance = total
            best_path = path

    return min_distance, best_path


# Test Case 1
cities1 = [(1,2), (4,5), (7,1), (3,6)]

dist, path = tsp(cities1)

print("Shortest Distance:", dist)
print("Shortest Path:", path)

# Test Case 2
cities2 = [(2,4), (8,1), (1,7), (6,3), (5,9)]

dist, path = tsp(cities2)

print("Shortest Distance:", dist)
print("Shortest Path:", path)