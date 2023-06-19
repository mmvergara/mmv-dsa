from dsa import *

def runningSum(self, nums: List[int]) -> List[int]:
    total = 0
    out = [0] * len(nums)
    for i in range(len(nums)):
        total+=nums[i]
        out[i] = total
    return out




res = runningSum("",[1,2,3,4,5])
print(res)
