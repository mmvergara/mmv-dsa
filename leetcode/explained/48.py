# Done Big O(n) = Space complexity o(n)
# array is rotating counter clockwise, rows become cols and vice versa

def rotate(self, matrix: list[list[int]]) -> None:
    # new arr with pre-allocate the size of the matrix
    new_arr = [0] * len(matrix)

    # create the rotate array
    for col in range(len(matrix[0])):
        subArr = [0] * len(matrix[0])
        i = 0

        for row in range(len(matrix)):
            index = len(matrix[0])-1-i 
            subArr[index] = (matrix[row][col])
            i+=1

        new_arr[col] = subArr
    
    # merge the new_arr with the original arr to modify it
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            matrix[row][col] = new_arr[row][col]

arr = [[1,2,3],[4,5,6],[7,8,9]]
res = rotate("",arr)

print(arr)
