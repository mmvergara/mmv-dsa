import time


def canCons(targetWord: str, wordBank: list):
    def rec(targetStr: str, memo={}):
        nonlocal wordBank
        if targetStr in memo:
            return memo[targetStr]
        if targetStr == "":
            return [[]]

        ways = []
        for w in wordBank:
            if targetStr.startswith(w):
                res = rec(targetStr[len(w) :])
                if res is not None:
                    ways.extend([[w] + x for x in res])
        memo[targetStr] = ways
        return ways

    print(rec(targetWord))


start_time = time.time()

# Step 3: Call the function

# Step 4: Record the end time
print(canCons("eeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee", "f", "eeeeeee"]))
end_time = time.time()
# print(canCons("purple", ["purp", "p", "ur", "le", "purpl"]))
print(end_time - start_time)
