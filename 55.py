from dsa import *


def canJump(self, nums: List[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        print(i + nums[i], goal)
        if i + nums[i] >= goal:
            goal = i
    if goal == 0:
        return True
    return False


canJump("", [2, 3, 0, 1, 4])
