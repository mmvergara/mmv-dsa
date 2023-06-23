# Done
def generateParenthesis(self, n: int) -> list[str]:
    subsets = []

    def dfs(l,r,s):
        # base case if the string is already at len = n*2 because there are only n pairs
        if len(s) == n*2:
            print(s)
            subsets.append(s)
            return
        
        # if l parenthesis is not n size then we still have some more pairs available
        if l < n:
            dfs(l+1,r,s+"(")

        # the r parenthesis should always match the l parenthesis length as two of these are pairs
        if r < l:
            dfs(l,r+1,s+")")

    dfs(1,0,"(")

    return subsets
        
'''
            (
            
    ((                ()

(())() ((()))        ()()() ()(())

'''


res = generateParenthesis("",3)
print(res)
