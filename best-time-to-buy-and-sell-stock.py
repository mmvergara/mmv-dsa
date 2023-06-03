import sys
def maxProfit(self, prices: list[int]) -> int:
      minimum = sys.maxsize
      maxProfit = 0
      for i in range(len(prices)):
            if prices[i] < minimum:
                  minimum = prices[i]
                  continue
            profit = prices[i] - minimum
            maxProfit = max(profit,maxProfit)
      return maxProfit
            


res = maxProfit("",[7,1,5,3,6,4]) 
print(res)
             
        

