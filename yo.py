
def twoSum(self, nums: list[int], target: int):
    coms = {}

    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in coms:
            return [i,comp[coms]]
        coms[nums[i]] = i

    pass


