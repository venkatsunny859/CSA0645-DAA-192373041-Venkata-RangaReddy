from itertools import permutations

cities = ['A', 'B', 'C', 'D', 'E']

dist = {
    ('A','B'):10, ('A','C'):15, ('A','D'):20, ('A','E'):25,
    ('B','C'):35, ('B','D'):25, ('B','E'):30,
    ('C','D'):30, ('C','E'):20,
    ('D','E'):15
}

# Make symmetric
for (u,v), d in list(dist.items()):
    dist[(v,u)] = d

min_cost = float('inf')
best_route = None

for perm in permutations(cities[1:]):
    route = ['A'] + list(perm) + ['A']
    cost = 0

    for i in range(len(route)-1):
        cost += dist[(route[i], route[i+1])]

    if cost < min_cost:
        min_cost = cost
        best_route = route

print("Route:", " -> ".join(best_route))
print("Distance:", min_cost)