def numDecodings(self, s: str) -> int:
    if len(s) == 0 or s[0] == "0":
        return 0
    combs = []

    def rec(combs, s, curS, i):
         if i >= len(s):
            combs.append(curS[:])
            return

        # either take one or take two
        rec(combs, s, curS + [s[i]], i + 1)

        if i < len(s) - 1:
            rec(combs, s, curS + [s[i] + s[i + 1]], i + 2)

    rec(combs, s, [], 0)
    print(combs)
    res = 0
    for comb in combs:
        print(f"for {comb}")
        add = 1
        for i in comb:
            if i[0] == "0":
                add = 0
                break
            i = int(i)
            if i <= 0 or i > 26:
                add = 0
                break
        print(f"added {add}")
        res += add
    print(res)
    return res


numDecodings("", "1111111111111111111111111111")
