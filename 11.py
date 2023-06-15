
def maxArea(self, height: list[int]) -> int:
    # start from outwards with left and right pointer
    # move the the pointer with the lowest value inwards until you can't move them anymore
    left = 0
    right = len(height)-1
    maxA = 0
    while left < right:
        minH = min(height[left],height[right])
        width = right - left
        
        maxA = max(minH*width,maxA)
        if height[left] < height[right]:
            left+=1
        else:
            right-=1

    return maxA


print(maxArea("",[1,8,6,2,5,4,8,3,7]))


