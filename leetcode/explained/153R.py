import sys
from dsa import *

def findMin(self, nums: List[int]) -> int:
    # initialize pointers
    left = 0
    right = len(nums)-1

    # set the lowest to be the first el incase there are only 1 element
    res = nums[0]

    while left <= right:
        # if the we are on a sorted part then the leftmost el will always be the lowest
        if nums[left] < nums[right]:
            res = min(res,nums[left])
            break
        
        # calculate mid index
        mid = (left+right) // 2

        # see if mid < than the last res
        res = min(res,nums[mid])

        # if the mid part is greater than the left element
        # it means that we are on the left portion of the array which are higher than right part 
        # so search right part
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1

    print(res)
    return res




findMin("",[3,4,5,1,2])
findMin("",[4,5,6,7,0,1,2])
findMin("",[11,13,15,17])
