def longestConsecutive(self, nums: list[int]) -> int:
    my_set = set(nums)
    max_consecutive = 0
    for n in my_set:
        cur = n
        total = 1
        # check if the number is not the a start of the sequence
        if n-1 in my_set:
            continue

        # if its not then the consecutiveness is still going
        while cur+1 in my_set:
            cur+=1
            total+=1

        # record the maximum consecutive based on total var
        max_consecutive = max(max_consecutive,total)

    return max_consecutive

        





res = longestConsecutive("",[100,4,200,1,3,2])
print(res)

