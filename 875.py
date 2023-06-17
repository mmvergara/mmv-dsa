

def minEatingSpeed(self, piles: list[int], h: int) -> int:
    left = 0
    right = max(piles)


    res = right
    while left < right:
        mid = (left+right) // 2
        arr = []
        for p in piles:
            arr.append(mid/p)
        print(mid)




minEatingSpeed("",[3,6,7,11],8)








