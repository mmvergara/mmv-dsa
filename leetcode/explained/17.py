from randoms.dsa import *


# def letterCombinations(self, digits: str) -> List[str]:
#     mp = {
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz",
#     }
#     res = [[]]

#     for n in digits:
#         newRes = []
#         for l in mp[n]:
#             print(l)
#             for c in res:
#                 apArr = c[:]
#                 if not apArr:
#                     apArr.append(l)
#                 else:
#                     apArr[0] += l
#                 newRes.append(apArr[0])
#         res = newRes

#     print(res)
from randoms.dsa import *


def letterCombinations(self, digits: str) -> List[str]:
    if digits == "":
        return []
    mp = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    res = []

    def rec(digits, i, res, curStr):
        if len(curStr) == len(digits):
            res.append(curStr[:])
            return
        for strs in mp[digits[i]]:
            rec(digits, i + 1, res, curStr + strs)

    rec(digits, 0, res, "")
    return res


letterCombinations("", "23")


letterCombinations("", "23")
