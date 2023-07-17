from dsa import *


def letterCasePermutation(self, s: str) -> List[str]:
    perms = set()

    def rec(s, i, curS: str):
        print(curS)
        if i == len(s):
            perms.add(curS[:])
            return
        rec(s, i + 1, curS[:].replace(curS[i], curS[i].upper()))
        rec(s, i + 1, curS[:])

    rec(s[:], 0, s[:].lower())
    return perms


r = letterCasePermutation("", "RmR")
print(r)
