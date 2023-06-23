# NOT DONE
def checkStraightLine(self, coords: list[list[int]]) -> bool:
    xr = abs(coords[0][0] - coords[1][0]) 
    yr = abs(coords[0][1] - coords[1][1])
    for i in range(len(coords)-1):
        if abs(coords[i][0]-coords[i+1][0]) != xr:
            return False
        if abs(coords[i][1]-coords[i+1][1]) != yr:
            return False
    return True



checkStraightLine("",[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
