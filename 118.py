
def generate(self, numRows: int) -> list[list[int]]:
    out = [[1]]
    for i in range(numRows-1):
        newRow = [1]
        for j in range(i):
            newRow.append(out[i][j]+out[i][j+1])
        newRow.append(1)
        out.append(newRow)
    return out




generate("",5)
