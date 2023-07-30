def canCons(targetWord: str, wordBank: list):
    def rec(targetStr, memo={}):
        nonlocal wordBank
        if targetStr in memo:
            return memo[targetStr]

        if targetStr == "":
            return 1

        totalCount = 0

        for w in wordBank:
            if len(w) == 0:
                continue
            if targetStr.startswith(w):
                totalCount += rec(targetStr[len(w) :])
        memo[targetStr] = totalCount
        return memo[targetStr]

    return rec(targetWord)


print(
    canCons(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
        ["e", "ee", "eee", "eeee", "eeeeee", "eeeeeeeeeeeeeeee", "f"],
    )
)
