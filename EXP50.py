# EXP50.py - Assembly Line Scheduling (2 lines) using DP

def assembly_line_min_time(n, a1, a2, t1, t2, e1, e2, x1, x2):
    """Find minimum time using DP for assembly line scheduling"""
    dp1 = [0] * n
    dp2 = [0] * n
    
    dp1[0] = e1 + a1[0]
    dp2[0] = e2 + a2[0]
    
    for i in range(1, n):
        dp1[i] = min(dp1[i-1], dp2[i-1] + t2[i-1]) + a1[i]
        dp2[i] = min(dp2[i-1], dp1[i-1] + t1[i-1]) + a2[i]
    
    return min(dp1[n-1] + x1, dp2[n-1] + x2)

print("=" * 60)
print("Assembly Line Scheduling Problem")
n = 4
a1 = [4, 5, 3, 2]
a2 = [2, 10, 2, 3]
t1 = [7, 4, 5, 0]
t2 = [9, 2, 8, 0]
e1 = 10
e2 = 12
x1 = 18
x2 = 7

print(f"Number of stations: {n}")
print(f"Line 1 times: {a1}")
print(f"Line 2 times: {a2}")

result = assembly_line_min_time(n, a1, a2, t1, t2, e1, e2, x1, x2)
print(f"\nMinimum time required: {result}")
print("=" * 60)
