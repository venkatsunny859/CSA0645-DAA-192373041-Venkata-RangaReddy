def game_of_life(board):

    rows = len(board)
    cols = len(board[0])

    directions = [
        (-1,-1),(-1,0),(-1,1),
        (0,-1),(0,1),
        (1,-1),(1,0),(1,1)
    ]

    copy = [row[:] for row in board]

    for r in range(rows):
        for c in range(cols):

            live = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    live += copy[nr][nc]

            if copy[r][c] == 1:
                if live < 2 or live > 3:
                    board[r][c] = 0
            else:
                if live == 3:
                    board[r][c] = 1

    return board

board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]

print(game_of_life(board))