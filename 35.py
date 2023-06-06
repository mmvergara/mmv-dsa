def searchInsert(self, nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right =  mid - 1
        else:
            left = mid + 1 
    return left
            

    


res = searchInsert("", [1,3,5,6], 5)
print(res)

