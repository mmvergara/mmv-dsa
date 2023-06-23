# Done
def generateParenthesis(self, n: int) -> list[str]:
    subsets = []

    def dfs(l,r,s):
        if len(s) == n*2:
            print(s)
            subsets.append(s)
            return
        if l < n:
            dfs(l+1,r,s+"(")
        if r < l:
            dfs(l,r+1,s+")")

    dfs(1,0,"(")

    return subsets
        



generateParenthesis("",3)
