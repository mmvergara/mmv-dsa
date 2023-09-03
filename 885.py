from randoms.dsa import *


def spiralMatrixIII(
    self, rows: int, cols: int, rStart: int, cStart: int
) -> List[List[int]]:
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    matrix[rStart][cStart] = 1

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    curLoc = [rStart, cStart]
    total = rows * cols
    l = 0
    num = 1
    i = 0
    while num < total:
        x = 1 if l == 0 else l
        for _ in range(x):
            dx, dy = dirs[i]
            newX = dx + curLoc[0]
            newY = dy + curLoc[1]

            if newX >= 0 and newX < rows and newY >= 0 and newY < cols:
                num += 1
                matrix[newX][newY] = num
            curLoc = [newX, newY]

        i += 1
        if i == 4:
            i = 0
        l += 1
        print(i)
        if num == 9:
            break

    n = len(matrix)
    for r in range(n):
        print(matrix[r])


spiralMatrixIII("", 5, 6, 1, 4)
