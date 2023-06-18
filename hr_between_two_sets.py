
def lcm(arr):
    a = max(arr)
    b = min(arr)

    multiples = set()
    lcm = None
    
    i = 1
    while not lcm:
        ap = a * i
        bp = b * i
        if bp in multiples:
            return bp
        multiples.add(ap)
        i+=1
    raise Exception("ERROR")

def commonfactors(arr):
    factors = {}
    for n in arr:
        for x in range(1,n+1):
            if n % x == 0:
                if x in factors:
                    factors[x]+=1
                else:
                    factors[x]=1
    out = []
    for k,v in factors.items():
        if v == len(arr):
            out.append(k)

    return out 

def getTotalX(a, b):
    lcms = lcm(a)
    cf = commonfactors(b)
    out = []
    for x in cf:
        if x % lcms == 0:
            out.append(x)
    return len(out)



getTotalX([2,6],[24,36])
