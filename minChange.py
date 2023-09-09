def minChange(amount, coins):
    mp = {}

    def rec(s=0, totalC=0, mp={}):
        if s > amount:
            return False
        if s == amount:
            return totalC
        ans = float("inf")

        for c in coins:
            res = rec(s + c, totalC + 1)
            if res:
                ans = min(ans, res)

        mp[s] = ans

        return mp[s]

    print(rec(0, 0, mp))
    print(mp)


minChange(7, [5, 3])
