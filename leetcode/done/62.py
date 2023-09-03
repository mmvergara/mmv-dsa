
def uniquePaths(self, m: int, n: int,memo={}) -> int:

    # see if we already solved this path
    if (m,n) in memo:
        return memo[(m,n)]
    if (n,m) in memo:
        return memo[(n,m)]
    
    # base cases
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    
    # memoized path taken
    res1 = memo[(m-1,n)] = uniquePaths("",m-1,n,memo)  
    res2 = memo[(m,n-1)] = uniquePaths("",m,n-1,memo)  
    
    return res1 + res2


res = uniquePaths("",3,7)
print(res)
            
