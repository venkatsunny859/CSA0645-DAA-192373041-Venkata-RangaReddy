from itertools import permutations

def total_cost(assignment, cost_matrix):

    cost = 0

    for worker, task in enumerate(assignment):
        cost += cost_matrix[worker][task]

    return cost


def assignment_problem(cost_matrix):

    n = len(cost_matrix)

    min_cost = float('inf')
    best_assignment = None

    for assignment in permutations(range(n)):

        cost = total_cost(assignment, cost_matrix)

        if cost < min_cost:
            min_cost = cost
            best_assignment = assignment

    return best_assignment, min_cost


# Test Case 1
cost_matrix1 = [
    [3,10,7],
    [8,5,12],
    [4,6,9]
]

assignment, cost = assignment_problem(cost_matrix1)

print("Optimal Assignment:", assignment)
print("Total Cost:", cost)


# Test Case 2
cost_matrix2 = [
    [15,9,4],
    [8,7,18],
    [6,12,11]
]

assignment, cost = assignment_problem(cost_matrix2)

print("Optimal Assignment:", assignment)
print("Total Cost:", cost)