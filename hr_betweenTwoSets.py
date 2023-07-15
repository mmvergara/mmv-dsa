def getCommonFactors(arr):
    factors = set([arr[0]])
    if len(arr) == 0:
        return []

    for i in range(1,arr[0]):
        if arr[0] % i == 0:
            factors.add(i)

    remove = set()
    for i in range(1,len(arr)):
        for f in factors:
            if arr[i] % f != 0:
                remove.add(f)

    return factors-remove

    


def getTotalX(a,b):
    res = set() 

    f = getCommonFactors(b)
    for n in f:
        if all([n%fc == 0 for fc in a]):
            res.add(n)
    
    return len(res)


res = getTotalX([3,4],[24,48])
print(res)
