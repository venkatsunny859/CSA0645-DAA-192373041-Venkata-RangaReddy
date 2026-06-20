# EXP84.py - Generalized N-Queens with Obstacles and Restricted Positions

def generalized_n_queens(n, m, obstacles=None, restricted=None):
    """N-Queens on n×m board with obstacles and restrictions"""
    if obstacles is None:
        obstacles = set()
    if restricted is None:
        restricted = {}
    
    solutions = []
    
    def is_safe(col_placement, row, col):
        if (row, col) in obstacles:
            return False
        if row in restricted and col not in restricted[row]:
            return False
        
        for i in range(row):
            if col_placement[i] == col or abs(col_placement[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(col_placement, row):
        if row == n:
            solutions.append(col_placement[:])
            return
        
        for col in range(m):
            if is_safe(col_placement, row, col):
                col_placement[row] = col
                backtrack(col_placement, row + 1)
    
    backtrack([-1] * n, 0)
    return solutions

print("=" * 70)
print("Generalized N-Queens with Obstacles and Restrictions")
print()

print("Test 1: 8×10 Board")
sols1 = generalized_n_queens(8, 10)
print(f"Solutions found: {len(sols1)}")
if sols1:
    print(f"One solution: {[s+1 for s in sols1[0]]}")
print()

print("Test 2: 5×5 Board with Obstacles at (2,2), (4,4)")
obstacles2 = {(2, 2), (4, 4)}
sols2 = generalized_n_queens(5, 5, obstacles2)
print(f"Solutions found: {len(sols2)}")
if sols2:
    print(f"One solution: {[s+1 for s in sols2[0]]}")
print()

print("Test 3: 6×6 Board (restricted columns for row 0)")
restricted3 = {0: [0, 2, 4]}
sols3 = generalized_n_queens(6, 6, restricted=restricted3)
print(f"Solutions found: {len(sols3)}")
if sols3:
    print(f"One solution: {[s+1 for s in sols3[0]]}")
print("=" * 70)
