from dsa import *


def alternatingSubarray(self, nums: List[int]) -> int:
    stack = []
    maxr = -1
    d = -1
    for i in range(1, len(nums)):
        x = nums[i] - nums[i - 1]
        if abs(x) != 1:
            stack = []
            d = -1
        else:
            if not stack and x == -1:
                continue

            if not stack or stack[-1] * -1 == x:
                stack.append(x)
                maxr = max(maxr, len(stack) + 1)
                d *= -1
            else:
                stack = [x]
                d = 1

    return maxr


print(alternatingSubarray("", [6, 12, 2, 3, 8, 9, 10, 10, 2, 1]))
# print(alternatingSubarray("", [14, 23, 19, 20, 2, 1, 13, 32, 30]))
# print(alternatingSubarray("", [2, 3, 4, 3, 4]))
# alternatingSubarray("", [3, 3, 3, 2, 3, 3, 2, 1, 1])
