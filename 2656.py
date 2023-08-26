
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        cur = max(nums)
        
        for i in range(k):
            cur += cur+1
        return cur


