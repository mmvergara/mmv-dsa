
def fib(n: int,memo={}) -> int:
    if n in memo:
        return memo[n]

    if n == 1:
        return 1
    if n == 0:
        return 0


    memo[n] = fib(n-2)+fib(n-1)
    return memo[n]

print(fib(12))


