from typing import List

def buyChoco(prices: List[int], money: int) -> int:
    # we cannot buy 2 chocolates if there is less than 2 elements in the array
    if len(prices) < 2:
        return money
    
    # we take the first two prices as a starting point before the loop
    first_lowest_index = 1
    second_lowest_index = 0

    # loop throught but skipping 2 elements as we get by
    for i in range(2, len(prices)):
        
        # determine which of the 2 holds the highest value and that will decide which index we will compare first to the current prices[i]
        if prices[first_lowest_index] < prices[second_lowest_index]:
            second_lowest_index = i if prices[i] < prices[second_lowest_index] else second_lowest_index
            first_lowest_index = i if prices[i] < prices[first_lowest_index] else first_lowest_index
        else:
            first_lowest_index = i if prices[i] < prices[first_lowest_index] else first_lowest_index
            second_lowest_index = i if prices[i] < prices[second_lowest_index] else second_lowest_index

    # calculate total prie
    total_cost = prices[first_lowest_index] + prices[second_lowest_index]

    # if our money is not enough and will lead to a negative value, then we return money
    if (money - total_cost ) < 0:
      return money
    
    # return change
    return money - total_cost 
