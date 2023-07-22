from dsa import *


def canJump(self, nums: List[int]) -> bool:
    def rec(i, dp={}):
        # print(f"start at {i}")
        if i in dp:
            return dp[i]
        if i >= len(nums) - 1:
            return True

        for j in range(i + 1, i + nums[i] + 1):
            print(j,i)
            if j + i >= len(nums) - 1:
                return True
            print(f"GOING in {j}")
            if rec(j, dp):
                return True

        dp[i] = False
        return dp[i]

    return rec(0, {})


# print(canJump("", [2, 3, 1, 1, 4]))
print(canJump("", []))
