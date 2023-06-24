
def staircase(n):
    for i in range(n):
        print(f'{" "*abs(i+1-n)}{"#"*(i+1)}')

staircase(4)
