from dsa import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] == target:
            return 1

        if target in nums:
            return 1

        minSA = float("-inf")

        l = 0
        r = 0
        curSum = nums[0]
        while r < len(nums) - 1:
            if curSum < target:
                r += 1
                if nums[r] == target:
                    return 1
                curSum += nums[r]

            if curSum > target:
                curSum -= nums[l]
                l += 1

            minSA = min(minSA, abs(l - r))

        return minSA
