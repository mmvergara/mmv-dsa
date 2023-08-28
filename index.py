def generateParenthesis(self,n):
    def rec(curS,l,r):
        if l == 0 and r == 0:
            print(curS)
            return
        if l == r:
            rec(curS+"(",l-1,r)
            return
        
        if l == 0:
            rec(curS+")",l,r-1)
            return

        if l < r:
            rec(curS+")",l,r-1)
        rec(curS+"(",l-1,r)
    rec("",n,n)

  
generateParenthesis(3)