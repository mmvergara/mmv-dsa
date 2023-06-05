def fib(n:int,memo:dict={}):
    if n in memo:
        print(f"{n} already done")
        return memo[n]
    if n == 1 or n == 0:
        return n
    res = fib(n-1) + fib(n-2)
    memo[n] = res
    return res
print(fib(15))