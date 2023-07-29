from dsa import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        # Initialize pointers, current sum, and minimum subarray length
        l, r = 0, 0
        curSum = nums[0]
        minSA = float("inf")

        while r < len(nums):
            if curSum >= target:
                minSA = min(minSA, r - l + 1)  # Update the minimum subarray length
                curSum -= nums[l]  # Move the left pointer to shrink the window
                l += 1
            else:
                r += 1  # Move the right pointer to expand the window
                if r < len(nums):
                    curSum += nums[r]

        return minSA if minSA != float("inf") else 0
