from dsa import *


def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    if n % 2 == 0:
        return
    dp = {}

    def backtract(n):
        if n in dp:
            return dp[n]

        if n == 0:
            return []
        if n == 1:
            return [TreeNode(0)]

        res = []

        for l in range(n):
            r = n - 1 - l
            leftTree = backtract(l)
            rightTree = backtract(r)

            for lt in leftTree:
                for rt in rightTree:
                    res.append(TreeNode(0, lt, rt))
        dp[n] = res
        return dp[n]

    return backtract(n)


print(allPossibleFBT("", 7))
