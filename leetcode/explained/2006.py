from randoms.dsa import *


def countKDifference(self, nums: List[int], k: int) -> int:
    mp = {}
    diffs = 0
    for i in range(len(nums)):
        if nums[i] in mp:
            mp[nums[i]] += 1
        else:
            mp[nums[i]] = 1

        print(mp, nums[i])

        if nums[i] - k in mp:
            diffs += mp[nums[i] - k]
        if nums[i] + k in mp:
            diffs += mp[nums[i] + k]
    return diffs


print(countKDifference("", nums=[1, 2, 2, 1], k=1))
