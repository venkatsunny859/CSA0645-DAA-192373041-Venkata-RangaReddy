import math

def closest_pair(points):

    min_distance = float('inf')
    closest_points = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):

            distance = math.sqrt(
                (points[i][0] - points[j][0]) ** 2 +
                (points[i][1] - points[j][1]) ** 2
            )

            if distance < min_distance:
                min_distance = distance
                closest_points = (points[i], points[j])

    return closest_points, min_distance


# Test Case
points = [(1, 2), (4, 5), (7, 8), (3, 1)]

pair, dist = closest_pair(points)

print("Closest Pair:", pair)
print("Minimum Distance:", dist)