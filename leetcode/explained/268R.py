# The missing number of nums in an unsorted list with length of n
# Create a set with range (length(nums))+1 because there is a 1 missing number
# loop through nums n+1 and if current num is not in nums that is the missing number
def missingNumber(self, nums: list[int]) -> int:
    for n in range(len(nums)+1):
        if n not in nums:
            return n