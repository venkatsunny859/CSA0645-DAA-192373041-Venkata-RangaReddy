# EXP83.py - N-Queens with Visualization

def solve_n_queens(n):
    """Solve N-Queens and visualize solutions"""
    solutions = []
    
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board, row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
    
    backtrack([-1] * n, 0)
    return solutions

def visualize_solution(solution):
    """Visualize a queen placement"""
    n = len(solution)
    for i in range(n):
        row = ['.' for _ in range(n)]
        row[solution[i]] = 'Q'
        print(' '.join(row))
    print()

print("=" * 60)
print("N-Queens Problem with Visualization")
print()

for n in [4, 5, 8]:
    solutions = solve_n_queens(n)
    print(f"N = {n}: Found {len(solutions)} solutions")
    if n <= 5:
        print(f"First solution:")
        visualize_solution(solutions[0])

print("=" * 60)
