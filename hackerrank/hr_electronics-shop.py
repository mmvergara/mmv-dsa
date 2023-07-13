def getMoneySpent(keyboards: list, drives: list, b):
    res = -1
    for k in keyboards:
        for d in drives:
            cSum = k+d
            if cSum == b:
                return cSum
            if cSum < b:
                res = max(res,cSum)
    return res

res = getMoneySpent([3, 2, 10], [5, 2, 8], 10)
print(res)
