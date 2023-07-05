from typing import List


def minPathSum(self, grid: List[List[int]]) -> int:

    # prefix sum first column
    print(grid)
    for i in range(1, len(grid)):
        grid[i][0] += grid[i - 1][0]

    # prefix sum first row
    print(grid)
    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i - 1]

    # traverse diagonally start from row 2 col 2
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
    return grid[-1][-1]
