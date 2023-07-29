from dsa import *


def canPartition(self, nums: List[int]) -> bool:
    # generate all of the subsets
    mp = {}

    def gen(i, subset, summ):
        nonlocal mp
        if i == len(nums):
            arrCopy = subset[:]

            if summ in mp:
                arrl = len(arrCopy)
                if arrl not in mp[summ]:
                    mp[summ][arrl] = [arrCopy]
                else:
                    mp[summ][arrl].append(arrCopy)
            else:
                mp[summ] = {len(arrCopy): [arrCopy]}
            return

        newS = summ + nums[i]
        gen(i + 1, subset + [(nums[i], i)], newS)
        gen(i + 1, subset, summ)

    gen(0, [], 0)

    for maps in mp.values():
        print("===")
        for n in maps.keys():
            complement = len(nums) - n
            if abs(complement) in maps:
                for subset1 in maps[abs(complement)]:
                    for subset2 in maps[n]:
                        possible = True
                        for _, i in subset1:
                            if not possible:
                                break
                            for _, j in subset2:
                                if i == j:
                                    possible = False
                                    break
                        if possible:
                            return True

    return False

    # create a mapping of subsets that have the same sums


res = canPartition(
    "",
    [
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        99,
        97,
    ],
)
print(res)
