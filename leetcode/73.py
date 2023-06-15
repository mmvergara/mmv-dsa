
def setZeroes(self, matrix: list[list[int]]) -> None:
    # find all of the 0's row and col index
    max_row = len(matrix)-1
    max_col = len(matrix[0])-1

    zeroes = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                zeroes.append((row,col))
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    def addT(tuple1,tuple2):
        return tuple(map(lambda i, j: i + j, tuple1, tuple2))
    
    def dfsC(coords,d):
        row = coords[0]
        col = coords[1]
        if row > max_row or col > max_col or row < 0 or col < 0:
            return

        matrix[row][col] = 0
        dfsC(addT(coords,d),d)
        

    for coords in zeroes:
        for d in directions:
            dfsC(coords,d)
    print(matrix)

setZeroes("",[[1,1,1],[1,0,1],[1,1,1]])
