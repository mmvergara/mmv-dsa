def moveZeroes(self, nums: list[int]) -> None:
    # Two pointer solution we're using two pointers to bubble up the zeroes to the end

    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            temp = nums[fast]
            nums[fast] = nums[slow]
            nums[slow] = temp
            slow+=1
        if nums[slow] != 0:
            slow+=1
        