

def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
    # sort the array
    nums.sort()
    
    # accumulation whatever the hell that is
    ls = 0
    for i in range(len(nums)):
        ls += nums[i]
        nums[i] = ls

    def binarySearch(arr:list[int],target)-> int:
        # returns the index where target can be inserted
        l = 0
        r = len(arr)

        while l < r:
            mid = (l+r) // 2
            if arr[mid] <= target:
                l = mid + 1
            else:
                r = mid

        return l

    # Binary search find at which index q in queries can be inserted in the nums arr while maintaining order
    return [binarySearch(nums,q) for q in queries]




res = answerQueries("",[76478,102343,247573,477461,430399,260435,250631,785081,904724,392720],[63736,339518,37262,108251,216825])

print(res)


