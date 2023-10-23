"2263"


def numDecodings(self, s: str) -> int:
    # each iteration take one or two then decode it

    def rec(count, i, dp={}):
        if i == len(s):
            return 1

        # take one
        one = int(s[i])
        two = int(s[i] + s[i])

        if one != 0:
            count += rec(count + 1, i + 1, dp)

        if one not in [1, 2]:
            return 0

        if two <= 26:
            count += rec(count + 1, i + 2, dp)

        dp[(count, i)] = count
        return count

    print(rec(0, 0))


numDecodings("", "2263")
