
def twoSum(self, nums: list[int], target: int) -> list[int]:
    complements = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in complements:
            j = complements[complement]
            return [i,j]
        else:
            complements[nums[i]] = i

    return []
        


