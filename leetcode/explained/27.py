# number of occurence of n != val
def removeElement(self, nums: list[int], val: int) -> int:
    i = 0
    for n in nums:
        if n != val:
            nums[i] = n
            i+=1
    return i
