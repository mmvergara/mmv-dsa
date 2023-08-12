from dsa import *

def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    mp = {}
    sNums = sorted(nums,reverse=True)
    for i in range(len(sNums)):
        mp[sNums[i]] = len(sNums)-i-1
    
    for i in range(len(nums)):
        nums[i] = mp[nums[i]]
    
    return nums


smallerNumbersThanCurrent("",[8,1,2,2,3])



