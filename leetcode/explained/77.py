from randoms.dsa import *


def combine(self, n: int, k: int) -> List[List[int]]:
    res = []

    def rec(res, comb, i):
        if len(comb) == k:
            res.append(comb[:])
            return

        for x in range(i, n + 1):
            rec(res, comb[:] + [x], x + 1)

    rec(res, [], 1)
    print(res)
    return res


combine("", 4, 2)
