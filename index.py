def matToGraph(mat):
    ROWS = len(mat)
    COLS = len(mat[0])
    g = {}

    def withinBounds(r, c):
        return 0 <= r and r < ROWS and 0 <= c and c < COLS

    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for r in range(ROWS):
        for c in range(COLS):
            g[(r, c)] = []
            for d in dirs:
                dx, dy = d
                neighborX = r + dx
                neighborY = c + dy
                if withinBounds(neighborX, neighborY):
                    neighborNode = {(neighborX, neighborY): mat[neighborX][neighborY]}
                    g[(r, c)].append(neighborNode)

    print(g)

    pass


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matToGraph(matrix)
