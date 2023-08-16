grid = [
    [0, 0, 4, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 7, 3, 4, 6, 0, 0],
    [0, 0, 3, 0, 2, 1, 0, 4, 9],
    [0, 3, 5, 0, 9, 0, 4, 8, 0],
    [0, 9, 0, 0, 0, 0, 0, 3, 0],
    [0, 7, 6, 0, 1, 0, 9, 2, 0],
    [3, 1, 0, 9, 7, 0, 2, 0, 0],
    [0, 0, 9, 1, 8, 2, 0, 0, 3],
    [0, 0, 0, 0, 6, 0, 1, 0, 0],
]


def isValid(grid, r, c, v):
    notInRow = v not in grid[r]

    # check if not in col
    notInCol = True
    for i in range(len(grid)):
        if v == grid[i][c]:
            notInCol = False
            break

    # check in boxes
    notInBoxes = True
    boxes = [
        {(0, 1), (1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)},
        {(2, 4), (0, 4), (1, 5), (0, 3), (1, 4), (2, 3), (0, 5), (2, 5), (1, 3)},
        {(0, 7), (2, 7), (1, 8), (0, 6), (1, 7), (2, 6), (1, 6), (0, 8), (2, 8)},
        {(4, 0), (3, 1), (5, 1), (4, 2), (3, 0), (5, 0), (3, 2), (4, 1), (5, 2)},
        {(4, 4), (5, 5), (3, 4), (4, 3), (5, 4), (4, 5), (3, 3), (5, 3), (3, 5)},
        {(3, 8), (5, 8), (3, 7), (4, 6), (5, 7), (5, 6), (4, 8), (3, 6), (4, 7)},
        {(6, 2), (7, 1), (8, 1), (6, 1), (7, 0), (8, 0), (7, 2), (6, 0), (8, 2)},
        {(7, 4), (8, 4), (6, 5), (6, 4), (7, 3), (8, 3), (7, 5), (6, 3), (8, 5)},
        {(8, 8), (7, 7), (8, 7), (6, 8), (6, 7), (7, 6), (8, 6), (6, 6), (7, 8)},
    ]

    for b in boxes:
        if (r, c) in b:
            for br, bc in b:
                if grid[br][bc] == v:
                    notInBoxes = False
                    break
        if not notInBoxes:
            break
    return notInBoxes and notInCol and notInRow


def solve(grid, r, c) -> list[list[int]]:
    print(grid)
    # if we are at the very end return true
    if r == 9:
        return True
    # if we're at the end of the col move on to the next row
    elif c == 9:
        return solve(grid, r + 1, 0)
    # if it's pre-filled move on
    elif grid[r][c] != 0:
        return solve(grid, r, c + 1)
    else:
        # if it is not pre-filled
        for k in range(1, 10):
            if isValid(grid, r, c, k):
                grid[r][c] = k
                # then continue solving
                if solve(grid, r, c + 1):
                    return True
                # if it's not possible change the num back to 0 and then retry
                grid[r][c] = 0


print(solve(grid=grid, r=0, c=0))


x = [
    [2, 6, 4, 8, 5, 9, 3, 1, 7],
    [9, 8, 1, 7, 3, 4, 6, 5, 2],
    [7, 5, 3, 6, 2, 1, 8, 4, 9],
    [1, 3, 5, 2, 9, 7, 4, 8, 6],
    [8, 9, 2, 5, 4, 6, 7, 3, 1],
    [4, 7, 6, 3, 1, 8, 9, 2, 5],
    [3, 1, 8, 9, 7, 5, 2, 6, 4],
    [6, 4, 9, 1, 8, 2, 5, 7, 3],
    [5, 2, 7, 4, 6, 3, 1, 9, 8],
]
