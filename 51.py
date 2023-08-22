def solveNQueens(self, n: int):
    cols = set()
    posDiags = set()  # (r + c)
    negDiags = set()  # (r - c)

    res = []
    board = [["."] * n for _ in range(n)]
    done = False

    def backtract(r):
        nonlocal done
        if done:
            return
        # if we are done which is r = n
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            print(board)
            done = True
            return

        for c in range(n):
            pd = r + c
            nd = r - c
            if c in cols or pd in posDiags or nd in negDiags:
                continue
            cols.add(c)
            posDiags.add(pd)
            negDiags.add(nd)
            board[r][c] = "Q"
            backtract(r + 1)
            cols.remove(c)
            posDiags.remove(pd)
            negDiags.remove(nd)
            board[r][c] = "."

    backtract(0)
    return res


solveNQueens("", 15)
