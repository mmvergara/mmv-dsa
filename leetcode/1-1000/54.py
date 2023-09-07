from randoms.dsa import *
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

    left,top = 0,0
    right,bot = len(matrix[0]),len(matrix)
    res = []
    while left < right:
        # get all top
        for i in range(left,right):
            res.append(matrix[top][i])
        top+=1

        for i in range(top,bot):
            res.append(matrix[i][right-1])
        right-=1

        for i in range(right-1,left-1,-1):
            res.append(matrix[bot-1][i])
            pass
        bot-=1

        for i in  range(bot-1,top-1,-1):
            res.append(matrix[i][left])
        left+=1
    return res
        









spiralOrder("",[[1,2,3],[4,5,6],[7,8,9]])
