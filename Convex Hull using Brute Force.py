def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - \
           (q[0] - p[0]) * (r[1] - q[1])


def brute_force_convex_hull(points):

    hull = []

    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):

            left = right = 0

            for k in range(n):

                if k == i or k == j:
                    continue

                val = orientation(points[i], points[j], points[k])

                if val > 0:
                    left += 1
                elif val < 0:
                    right += 1

            if left == 0 or right == 0:
                hull.append(points[i])
                hull.append(points[j])

    hull = list(set(hull))
    return hull


points = [
    (10,0), (11,5), (5,3), (9,3.5),
    (15,3), (12.5,7), (6,6.5), (7.5,4.5)
]

print(brute_force_convex_hull(points))