from dsa import *


def spiralMatrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    
    matrix = [[-1 for _ in range(n)] for x in range(m)]

    getNextDir = {"right": "bottom", "bottom": "left", "left": "top", "top": "right"}
    dirsVal = {"right": (0, 1), "bottom": (1, 0), "left": (0, -1), "top": (-1, 0)}
    visited = set()

    def dfs(r, c, lastDir):

        if (r, c) in visited:
            return
        visited.add((r, c))

        if head == None:
            return
        
        currentVal = head
        head = head.next
        matrix[r][c] = currentVal.val

        # try traversing into the last dir

        newLoc = (r + dirsVal[lastDir][0], c + dirsVal[lastDir][1])
        # if traversing into the last dir is out of bounds go to the next dir
        if newLoc[0] < 0 or newLoc[0] >= m or newLoc[1] < 0 or newLoc[1] >=n:
            newLoc = (r + dirsVal[getNextDir[lastDir]][0],c+dirsVal[getNextDir[lastDir]][1])
        else:
            dfs(newLoc[0],newLoc[1])
            return
        # if traversing to the new dir is out of bounds also dont travese
        if newLoc[0] < 0 or newLoc[0] >= m or newLoc[1] < 0 or newLoc[1] >=n:
            return
        else:
          dfs(newLoc[0],newLoc[1],getNextDir[lastDir])
          return
    dfs(0,0,"right")
    print(matrix)
        
    pass


spiralMatrix(3, 5, [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
