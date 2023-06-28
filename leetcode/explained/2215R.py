from typing import List

def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    # turn both array to set
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    # - operator on set will find the difference between them
    return [list(nums1_set - nums2_set), list(nums2_set - nums1_set)]


print(findDifference("", [1, 2, 3, 3], [1, 1, 2, 2]))
