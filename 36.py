def isValidSudoku(self, board: list[list[str]]) -> bool:
    # validate rows
    for i in range(len(board)):
        rowData = set()
        for el in board[i]:
            if el in rowData and el.isnumeric():
                print("falsse2")
                return False
            else:
                rowData.add(el)
    # validate cols
    for i in range(len(board)):
        row = i
        colData = set()
        print("=======")
        for j in range(9):
            data = board[j][row]
            print(data)
            if data in colData and data.isnumeric():
                return False
            else:
                colData.add(data)
        print("=======")

    # valid 3x3 grids
    centers = [
        (1, 1),
        (1, 4),
        (1, 7),
        (4, 1),
        (4, 4),
        (4, 7),
        (7, 1),
        (7, 4),
        (7, 7),
    ]
    directions = [
        (-1, 0),  # Up
        (-1, 1),  # Up-right
        (0, 1),  # Right
        (1, 1),  # Down-right
        (1, 0),  # Down
        (1, -1),  # Down-left
        (0, -1),  # Left
        (-1, -1),
    ]  # Up-left

    for i in range(len(centers)):
        c_row = centers[i][0]
        c_col = centers[i][1]
        gridData = [board[c_row][c_col]]
        for r, c in directions:
            new_r = c_row + r
            new_c = c_col + c
            data = board[new_r][new_c]
            if data in gridData and data.isnumeric():
                print(data, gridData)
                return False
            else:
                gridData.append(data)

    return True
