from dsa import *


def search(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        # if left portion is sorted:
        if nums[l] <= nums[m]:
            if target < nums[m] and target > nums[l]:
                r = m - 1
            else:
                l = m + 1

        # if right portion is sorted
        if nums[r] >= nums[m]:
            if target > nums[m] and target < nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


# x = [7,8,9,10,11,12,13,1,2,3,4]
x = [1]
res = search("", x, 1)
print(res)
