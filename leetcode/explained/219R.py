from dsa import *

def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # hash to store all seen values
    hset = {}

    for i in range(len(nums)):

        # if values in set
        if nums[i] in hset:

            # grab the index
            j = hset[nums[i]]

            # see if the current index and last same val index is <= K
            if abs(i-j) <= k:
                return True

   
        hset[nums[i]] = i

    return False

