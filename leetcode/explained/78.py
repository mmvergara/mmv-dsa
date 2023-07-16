from dsa import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def rec(nums, i, subset, subsets):
            if i == len(nums):
                subsets.append(subset[:])
                return

            rec(nums, i + 1, subset + [nums[i]], subsets)
            rec(nums, i + 1, subset, subsets)

        rec(nums, 0, [], subsets)
        return subsets
