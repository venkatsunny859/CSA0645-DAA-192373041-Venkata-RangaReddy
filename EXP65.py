# EXP65.py - Mouse and Cat Game

def cat_mouse_game(graph):
    """Determine winner of mouse vs cat game"""
    n = len(graph)
    DRAW = 0
    MOUSE_WIN = 1
    CAT_WIN = 2
    
    color = [[[0] * 2 for _ in range(n)] for _ in range(n)]
    degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]
    
    for m in range(n):
        for c in range(n):
            degree[m][c][0] = len(graph[m])
            degree[m][c][1] = len(graph[c]) if c != 0 else len(graph[c]) - 1
    
    queue = []
    for i in range(n):
        for t in range(2):
            if i > 0:
                color[0][i][t] = MOUSE_WIN
                queue.append((0, i, t, MOUSE_WIN))
            if i > 0:
                color[i][i][t] = CAT_WIN
                queue.append((i, i, t, CAT_WIN))
    
    while queue:
        mouse, cat, turn, result = queue.pop(0)
        
        if turn == 0:
            for prev_cat in graph[cat]:
                if color[mouse][prev_cat][1] == 0:
                    if result == MOUSE_WIN:
                        color[mouse][prev_cat][1] = MOUSE_WIN
                        queue.append((mouse, prev_cat, 1, MOUSE_WIN))
                    else:
                        degree[mouse][prev_cat][1] -= 1
                        if degree[mouse][prev_cat][1] == 0:
                            color[mouse][prev_cat][1] = CAT_WIN
                            queue.append((mouse, prev_cat, 1, CAT_WIN))
        else:
            for prev_mouse in graph[mouse]:
                if color[prev_mouse][cat][0] == 0:
                    if result == CAT_WIN:
                        color[prev_mouse][cat][0] = CAT_WIN
                        queue.append((prev_mouse, cat, 0, CAT_WIN))
                    else:
                        degree[prev_mouse][cat][0] -= 1
                        if degree[prev_mouse][cat][0] == 0:
                            color[prev_mouse][cat][0] = MOUSE_WIN
                            queue.append((prev_mouse, cat, 0, MOUSE_WIN))
    
    return color[1][2][0] if color[1][2][0] != 0 else DRAW

print("=" * 60)
print("Mouse and Cat Game")
print()

print("Test Case 1:")
graph1 = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
result1 = cat_mouse_game(graph1)
print(f"Graph: {graph1}")
print(f"Output: {result1} (0=Draw, 1=Mouse wins, 2=Cat wins)")
print()

print("Test Case 2:")
graph2 = [[1, 3], [0], [3], [0, 2]]
result2 = cat_mouse_game(graph2)
print(f"Graph: {graph2}")
print(f"Output: {result2}")
print("=" * 60)
