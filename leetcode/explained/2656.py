from randoms.dsa import *
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        cur = max(nums)
        
        for _ in range(k):
            cur += cur+1
        return cur


