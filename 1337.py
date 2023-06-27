
def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
    for i in range(len(mat)):
        mat[i] = (i,sum(mat[i]))
    arr = sorted(mat, key=lambda x: x[1])
    return [arr[i][0] for i in range(k)]
        
    
    # sort the array based on the number of soldiers in a row
    



res =kWeakestRows("",[[1,1,0,0,0],
     [1,1,1,1,0],
      [1,0,0,0,0],
       [1,1,0,0,0],
        [1,1,1,1,1]],3)

print(res)
