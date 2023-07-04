def addT(t1, t2):
    result = (t1[0] + t2[0], t1[1] + t2[1])
    return result

def snail(arr):
    if len(arr[0]) == 0:
        return []
    res = []
    ROWS = len(arr)
    COLS = len(arr[0])

    gNewDir = {
            "bottom":"left",
            "left":"top",
            "top":"right",
            "right":"bottom"
            }

    dirs = {
            "left":(0,-1),
            "right":(0,1),
            "top":(-1,0),
            "bottom":(1,0),
            }
    visitedPaths = set() 
    def dfs(r,c,lastDir): 
        # append the currentDir 
        visitedPaths.add((r,c))
        res.append(arr[r][c])

        # try going in the last Direction
        newLoc = addT((r,c),dirs[lastDir])
        newLocInBounds =newLoc[0] >= 0 and newLoc[0] < ROWS and newLoc[1] >= 0 and newLoc[1] < COLS
        if newLocInBounds and newLoc not in visitedPaths:
            dfs(newLoc[0],newLoc[1],lastDir)
            return
        
        # if not possible go to nextDirection
        newLoc = addT((r,c),dirs[gNewDir[lastDir]])
        newLocInBounds =newLoc[0] >= 0 and newLoc[0] < ROWS and newLoc[1] >= 0 and newLoc[1] < COLS
        if newLocInBounds and newLoc not in visitedPaths:
            dfs(newLoc[0],newLoc[1],gNewDir[lastDir])




        

    dfs(0,0,"right")
    print(res)
        # else proceed to next dir




    
    pass


snail([[1,2,3],
        [4,5,6],
        [7,8,9]])


