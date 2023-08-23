class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        cur = [nums[0],None]
        res = []
        for i in range(1,len(nums)):
            curNum = nums[i]
            prev = nums[i-1]
            if (prev+1) != curNum:
                cur[1] = prev
                if cur[0] == cur[1]:
                    res.append(str(cur[0]))
                    cur = [curNum,None]
                    continue
                res.append(f"{cur[0]}->{cur[1]}")
                cur = [curNum,None]
                continue
            cur[1] = curNum

        if cur[1] is not None:
            res.append(f"{cur[0]}->{cur[1]}")
        elif cur[0] is not None:
            res.append(str(cur[0]))
        return res
