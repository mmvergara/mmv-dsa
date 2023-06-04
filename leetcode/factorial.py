def factorial(n:int):
    if n in [0,1]:
        return 1
    return n * factorial(n-1)
print(factorial(8))