from randoms.dsa import *


def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
    res = [[None for _ in range(1, len(grid[0]) - 1)] for _ in range(1, len(grid) - 1)]
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            res[r - 1][c - 1] = max(
                grid[r][c],  # center
                grid[r - 1][c],  # top
                grid[r + 1][c],  # bot
                grid[r][c - 1],  # left
                grid[r][c + 1],  # right
                grid[r + 1][c + 1],  # bot right
                grid[r - 1][c - 1],  # top left
                grid[r + 1][c - 1],  # bot left
                grid[r - 1][c + 1],  # top right
            )
    return res


largestLocal("", [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]])
