import math

def minEatingSpeed(self, piles: list[int], h: int) -> int:
    # k = eating speed
    left = 1
    right = max(piles)
    res = right
    
    while left <= right:
        k = (left+right) // 2
        htta = 0

        for p in piles:
            htta += math.ceil(p/k)

        if htta <= h:
            res = min(res,k)
            right = k - 1
        else:
            left = k + 1

    return res 

res = minEatingSpeed("",[30,11,23,4,20],5)
print(res)
