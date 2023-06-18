
def solve(a, b):
    ap,bp = 0,0
    for i in range(len(a)):
        if a[i] > b[i]:
            ap+=1
        else:
            bp+=1
    return [ap,bp]

