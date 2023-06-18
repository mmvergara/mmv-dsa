
def kangaroo(x1, v1, x2, v2):
    diff = abs(x1 - x2)
    i=0
    while i != 11:
        x1 += v1
        x2 += v2
        if x1 == x2: return "YES" 
        i+=1
    return "NO" 
