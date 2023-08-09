def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    dp = {}

    def rec(i, j):
        print(i, j)
        if (i, j) in dp:
            return dp[(i, j)]

        if i + j == len(s3):
            return True

        res = False

        if i < len(s1) and s1[i] == s3[i + j]:
            if rec(i + 1, j):
                res = True
        if j < len(s2) and s2[j] == s3[i + j]:
            if rec(i, j + 1):
                res = True
        dp[(i, j)] = res
        return res

    return rec(0, 0)
