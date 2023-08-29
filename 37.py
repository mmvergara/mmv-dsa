from random.dsa import *


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # inside code validator
        # https://gist.github.com/syphh/62e6140361feb2d7196f2cb050c987b3
        def is_valid(grid, r, c, k):
            k = str(k)
            not_in_row = k not in grid[r]
            not_in_column = k not in [grid[i][c] for i in range(9)]
            not_in_box = k not in [
                grid[i][j]
                for i in range(r // 3 * 3, r // 3 * 3 + 3)
                for j in range(c // 3 * 3, c // 3 * 3 + 3)
            ]
            return not_in_row and not_in_column and not_in_box

        def solve(r, c):
            if r == 9:
                return board

            if c == 9:
                return solve(r + 1, 0)

            if board[r][c] != ".":
                return solve(r, c + 1)

            for n in range(1, 10):
                if is_valid(board, r, c, n):
                    board[r][c] = str(n)
                    res = solve(r, c + 1)
                    if res:
                        return res
                    else:
                        board[r][c] = "."

            return False

        return solve(0, 0)
