def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    curRow, curCol = rStart, cStart
    curNum = 1
    dirIdx = 0
    iterLen = 1
    res = [[rStart, cStart]]
    while curNum < rows * cols:
        dr, dc = directions[dirIdx]
        for c in range(iterLen):
            newR = curRow + dr
            newC = curCol + dc

            if 0 <= newR < rows and 0 <= newC < cols:
                curNum += 1
                res.append([newR, newC])
            curRow = newR
            curCol = newC

        dirIdx = (dirIdx + 1) % 4
        if dirIdx % 2 == 0:  # Increase iterLen every two directions
            iterLen += 1

    return res


result = spiralMatrixIII("", 5, 6, 1, 4)
print(result)
