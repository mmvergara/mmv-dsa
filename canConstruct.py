def canCons(targetWord: str, wordBank: list):
    def rec(targetStr, memo={}):
        nonlocal wordBank

        if targetStr in memo:
            return memo[targetStr]

        if targetStr == "":
            return True

        for w in wordBank:
            if w == "":
                continue
            if targetStr.startswith(w):
                if rec(targetStr[len(w) :], memo):
                    memo[targetStr] = True
                    return memo[targetStr]
        memo[targetStr] = False
        return memo[targetStr]

    return rec(targetWord)


print(
    canCons(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeeee", "eeeeeeeeeeeeeeee", ""],
    )
)
