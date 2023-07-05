
def maximumCount(self, arr: list[int]) -> int:
    l = 0
    r = len(arr)-1

    pointer = 0
    # perform binary search
    while l <= r:
        m = (l+r) // 2

        # get the index of an integer >= 0
        if arr[m] >= 0:
            pointer = m

        if arr[m] < 0:
            l = m + 1
        else:
            r = m - 1
    
    # mc = move count
    mc = 0
    # since 0 doesnt count as negative and positive integer we have to traverse until the value != 0
    while arr[pointer] == 0:
        pointer+=1
        # if we reached the end of the array and we did not find a value greater than > 0
        if pointer >= len(arr):
            # we return this which is number of negative numbers
            return pointer-1-mc
        mc+=1

    # return the max between postive and negative numbers
    return max(len(arr)-pointer,pointer-mc)
    



res = maximumCount("",[-1])
print(res)

