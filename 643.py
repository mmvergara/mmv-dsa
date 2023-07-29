
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return False

        curSum = sum([nums[i] for i in range(k)])
        maxAvg = curSum / k
        l = 0
        r = k
        
        while r < len(nums):
            curSum -= nums[l]
            l+=1
            curSum += nums[r]
            r+=1
            maxAvg = max(maxAvg, curSum/k)
            


        
        return maxAvg



        
