from randoms.dsa import *


# Learnings
# When dealing with duplicate values hasmap and sets must always be taken into considerations
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    ans = []
    mp = {}
    for i in range(len(nums)):
        if nums[i] in mp:
            mp[nums[i]] += 1
        else:
            mp[nums[i]] = 1

    def rec(comb=[]):
        if len(comb) == len(nums):
            ans.append(comb[:])
            return

        for k in mp.keys():
            if mp[k] == 0:
                continue
            comb.append(mp[k])
            mp[k] -= 1

            rec(comb)

            comb.pop()
            mp[k] += 1

    rec()
    return ans


print(permuteUnique("", [1, 1, 3]))
