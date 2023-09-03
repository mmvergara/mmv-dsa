import math 

def targetIndices(self, nums: list[int], target: int) -> list[int]:
    nums.sort()
    l = 0 
    r = len(nums)-1

    pointer = None

    # Perform binary search and store the num index in a pointer
    while l <= r:
        m = (l+r) // 2
        if nums[m] == target:
            pointer = m
            break
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    
    # if there is no pointer then we did not find the element
    if pointer is None:
        return []
    
    indexes = []

    # traverse leftward
    lwPointer = pointer
    while lwPointer > 0:
        lwPointer-=1
        if nums[lwPointer] != target:
            break
        indexes.insert(0,lwPointer)
    
    #input the middle pointer ( binary search result )
    indexes.append(pointer)

    # traverse rightward
    rwPointer = pointer
    while rwPointer < len(nums)-1:
        rwPointer+=1
        if nums[rwPointer] != target:
            break
        indexes.append(rwPointer)

    return indexes

res = targetIndices("",[1,2,5,2,3],5)
print(res)

