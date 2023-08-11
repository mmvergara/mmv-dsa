
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    N = len(candies)
    # get max
    maxC = max(candies)

    ans = [None for _ in range(N)]

    for i in range(N):
        ans[i] = (candies[i]+extraCandies) >= maxC
    print(ans)
    return ans
