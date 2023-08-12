def numJewelsInStones(self, jewels: str, stones: str) -> int:
    st = set(jewels)
    ans = 0

    for s in stones:
        if s in st:
            ans += 1

    return ans


numJewelsInStones("", jewels="aA", stones="aAAbbbb")
