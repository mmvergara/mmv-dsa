def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    brute force is just to sort the array backwards

    uses 2 pointers.
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            temp = nums[fast]
            nums[fast] = nums[slow]
            nums[slow] = temp
            slow+=1
        if nums[slow] != 0:
            slow+=1
        