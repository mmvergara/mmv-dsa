def travel_chessboard(s):
    # get the width and height of the matrix
    point1 = tuple(map(int, s[1:4].split(" ")))
    point2 = tuple(map(int, s[6:9].split(" ")))
    m = max(point1[0], point2[0]) - min(point1[0], point2[0]) + 1
    n = max(point1[1], point2[1]) - min(point1[1], point2[1]) + 1

    # m should be the lowest
    if m > n:
        m, n = n, m
    # create the matrix
    matrix = [[0] * m] * n

    # fill up the first row with 1's
    matrix[0] = [1] * n

    # fill up the first cols with 1's
    for i in range(n):
        matrix[i][0] = 1
    print(matrix)

    # calculate the paths
    for r in range(1, n):
        for c in range(1, m):
            print(r, c)
            matrix[r][c] = matrix[r - 1][c] + matrix[r][c - 1]

    return matrix[-1][-1]


res = travel_chessboard("(1 2)(8 7)")

print(res)
