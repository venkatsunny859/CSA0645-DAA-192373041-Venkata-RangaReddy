from functools import lru_cache

def catMouseGame(graph):
    n = len(graph)

    @lru_cache(None)
    def dfs(mouse, cat, turn):

        if mouse == 0:
            return 1

        if mouse == cat:
            return 2

        if turn > 2 * n * n:
            return 0

        if turn % 2 == 0:
            result = 2
            for nxt in graph[mouse]:
                state = dfs(nxt, cat, turn + 1)
                if state == 1:
                    return 1
                if state == 0:
                    result = 0
            return result

        else:
            result = 1
            for nxt in graph[cat]:
                if nxt == 0:
                    continue

                state = dfs(mouse, nxt, turn + 1)

                if state == 2:
                    return 2

                if state == 0:
                    result = 0

            return result

    return dfs(1, 2, 0)