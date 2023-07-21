import sys

def maxProfit(self, prices: list[int]) -> int:
    minimum = sys.maxsize
    maxProfit = 0
    for i in range(len(prices)):
        # keep tract of the min price
        if prices[i] < minimum:
            minimum = prices[i]
            # we continue because we just got a new min buy
            continue
        # calc the profit
        profit = prices[i] - minimum
        # update the profit if we found a better profit
        maxProfit = max(profit, maxProfit)
    return maxProfit


res = maxProfit("", [7, 1, 5, 3, 6, 4])
print(res)
