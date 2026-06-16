lines = [
    [5, 9, 3],
    [6, 8, 4],
    [7, 6, 5]
]

transfer = [
    [0, 2, 3],
    [2, 0, 4],
    [3, 4, 0]
]

stations = 3
dp = [lines[i][0] for i in range(3)]

for s in range(1, stations):
    new_dp = [float('inf')] * 3

    for curr in range(3):
        for prev in range(3):
            cost = dp[prev] + transfer[prev][curr] + lines[curr][s]
            new_dp[curr] = min(new_dp[curr], cost)

    dp = new_dp

print("Minimum Production Time =", min(dp))