def diagonalSum(self, mat: list[list[int]]) -> int:
    arr_length = len(mat)
    total = 0
    for row in range(arr_length):
        total += mat[row][row]
        total += mat[row][arr_length - 1 - row]
    if arr_length & 1:
        # if there is a center -1 on it
        total -= mat[arr_length // 2][arr_length // 2]
    return total