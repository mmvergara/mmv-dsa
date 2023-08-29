from randoms.dsa import *


def largestPerimeter(self, nums: List[int]) -> int:
    if len(nums) < 3:
        return 0
    nums.sort(reverse=True)

    def getP(a, b, c):
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return 0
        return a + b + c

    for i in range(2, len(nums)):
        res = getP(nums[i], nums[i - 1], nums[i - 2])
        if res != 0:
            return res
    return 0


largestPerimeter("", [1, 2, 1, 10])
