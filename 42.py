
def trap(self, height: list[int]) -> int:
    n = len(height)
    drops = 0

    lr = [0] * n

    maxr = [0] * n
    curmxr = 0

    for i in reversed(range(n-1)):
        curmxr = max(curmxr,height[i+1])
        maxr[i] = curmxr
    
    leftmax = 0
    for i in range(1,n-1):
        leftmax = max(leftmax,height[i])
        print(leftmax,height[i])
        




    return drops




trap("",[0,1,0,2,1,0,1,3,2,1,2,1])

#trap("",[4,2,0,3,2,5])
#trap("",[4,2,3])
