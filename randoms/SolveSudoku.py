board = [
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 9, 6, 7, 0, 0, 1, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 7, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 8, 0, 0, 0],
    [0, 0, 7, 9, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 4, 0, 0, 5],
]


def isValid(board, r, c, v):
    notInRow = v not in board[r]

    # check if not in col
    notInCol = True
    for i in range(len(board)):
        if v == board[i][c]:
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
                if board[br][bc] == v:
                    notInBoxes = False
                    break
        if not notInBoxes:
            break
    return notInBoxes and notInCol and notInRow


def solve(board):
    def rec(board, r, c):
        n = len(board)

        if c >= n:
            return rec(board, r + 1, 0)

        if r == n:
            print(board)
            return True

        if board[r][c] != 0:
            return rec(board, r, c + 1)

        for v in range(1, 10):
            if isValid(board, r, c, v):
                board[r][c] = v
                if rec(board, r, c + 1):
                    return True
                board[r][c] = 0
        return False

    return rec(board, 0, 0)


print(solve(board=board))
