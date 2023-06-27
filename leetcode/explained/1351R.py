
def countNegatives(self, grid: list[list[int]]) -> int:
    count = 0
    for arr in grid:
        for i in range(len(arr)-1,-1,-1):
            if arr[i] >= 0:
                break
            count+=1
    return count 


arr = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

res = countNegatives("",arr)
print(res)
