# In a 2D square array, find the sum of the diagonals
def diagonalSum(self, mat: list[list[int]]) -> int:
    arr_length = len(mat)
    total = 0
    # iterate through the rows
    for row in range(arr_length):
        # add the diagonal elements
        total += mat[row][row]
        # add the other diagonal elements from the other end of the array
        total += mat[row][arr_length - 1 - row]

    # if the array length is odd then we have to remove the center element
    if arr_length & 1:
        # if there is a center -1 on it
        total -= mat[arr_length // 2][arr_length // 2]
    
    # return the total
    return total