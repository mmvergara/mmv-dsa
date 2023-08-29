from randoms.dsa import *

# get first val,
# incremenet count if the res == n and decrement if not.. and after it if the count == 0  then the new counter starts at 1 and res = n


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
