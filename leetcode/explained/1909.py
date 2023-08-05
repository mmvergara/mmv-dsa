from dsa import *


# Learned, make use of indices and the logic behind a certain concept and obvious facts in this case it is sorted
def canBeIncreasing(self, nums: List[int]) -> bool:
    remove_count = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            remove_count += 1
            # If more than one element needs to be removed, return False directly.
            if remove_count > 1:
                return False
            # If the current element is less than or equal to i-2,
            # we have to remove the current element, so we set it to the previous number.
            if i > 1 and nums[i] <= nums[i - 2]:
                nums[i] = nums[i - 1]

    return True


canBeIncreasing("", [1, 2, 10, 5, 7])
