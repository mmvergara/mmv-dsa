from dsa import *


def maxArrayValue(self, nums: List[int]) -> int:
    stack = []
    for num in nums:
        while stack and stack[-1] <= num:
            num += stack.pop()
        stack.append(num)

    return max(stack)



res = maxArrayValue("", [34, 95, 50, 12, 25, 100, 21, 3, 25, 16, 76, 73, 93, 46, 18])
print(res)
