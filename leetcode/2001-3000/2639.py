def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
    COLS = len(grid[0])
    colsW = [0] * COLS
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            colsW[c] = max(colsW[c], len(str(grid[r][c])))

    return colsW
