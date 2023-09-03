
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def rec(nums,i,cur):
            if i == len(nums):
                return cur

            return rec(nums,i+1,cur) + rec(nums,i+1,cur ^ nums[i])
        return rec(nums,0,0)
