from dsa import *

# learned: for list that we know that are going to be filled with n values, we can optimize more by initializing an array with ex.[None for _ in range(i + 1)]


def generate(self, numRows: int) -> list[list[int]]:
    if numRows == 0:
        return []
    ans = [[1]]
    for i in range(1, numRows):
        last = ans[-1]
        new = [None for _ in range(i + 1)]
        new[0] = new[-1] = 1
        for j in range(1, i):
            new[j] = last[j - 1] + last[j]
        ans.append(new)
    return ans


print(generate("", 5))
