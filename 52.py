class Solution:
    def totalNQueens(self, n: int):
        cols = set()
        posDiags = set()  # (r + c)
        negDiags = set()  # (r - c)

        board = [["."] * n for _ in range(n)]

        def backtract(r):
            # if we are done which is r = n
            if r == n:
                return 1

            res = 0
            for c in range(n):
                pd = r + c
                nd = r - c
                if c in cols or pd in posDiags or nd in negDiags:
                    continue
                cols.add(c)
                posDiags.add(pd)
                negDiags.add(nd)
                board[r][c] = "Q"
                res += backtract(r + 1)
                cols.remove(c)
                posDiags.remove(pd)
                negDiags.remove(nd)
                board[r][c] = "."
            return res

        return backtract(0)
