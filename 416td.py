from dsa import *


def canPartition(self, nums: List[int]) -> bool:
    # shrink array
    f = {}
    for n in nums:
        if n in f:
            f[n] += 1
        else:
            f[n] = 1
    nums = []
    for k, v in f.items():
        if v % 2 == 0:
            nums.append(k)
            nums.append(k)
        else:
            if v >= 3:
                nums.append(k)
                nums.append(k)
                nums.append(k)
            else:
                nums.append(k)

    s = sum(nums)
    t = s // 2
    dp = {}

    def rec(i, t):
        if (i, t) in dp:
            return dp[(i, t)]
        if t == 0:
            return True
        if t < 0:
            return False

        if i == len(nums):
            return False

        dp[(i + 1, t - nums[i])] = rec(i + 1, t - nums[i])
        dp[(i + 1, t)] = rec(i + 1, t)
        return all([dp[(i + 1, t - nums[i])], dp[(i + 1, t)]])

    return rec(i=0, t=t)


res = canPartition("", [1, 2, 3, 5, 5])
print(res)
