from randoms.dsa import *

def decompressRLElist(self, nums: List[int]) -> List[int]:
    ans = []
    for i in range(0,len(nums),2): 
        for j in range(nums[i]):
            ans.append(nums[i+1])
    return ans

decompressRLElist("",[1,2,3,4])



