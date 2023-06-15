from dsa import *


def majorityElement(self, nums: List[int]) -> int:
    count = 0
    res = nums[0]
    for n in nums:
        if res == n:
            count += 1
        else:
            count -= 1

        if count == 0:
            res = n
            count = 1

    return res
