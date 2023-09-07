def countVowelStrings(self, n: int) -> int:
    arr = ["a", "e", "i", "o", "u"]

    def rec(strr="", j=0):
        if len(strr) == n:
            return 1
        res = 0
        for i in range(j, len(arr)):
            res += rec(strr[:] + arr[i], i)
        return res

    return rec


countVowelStrings("", 33)
