
def dashatize(n):
    
    if n is None:
        return "None"

    #convert int to arr
    n = list(str(abs(n)))
    
    if len(n) == 1:
        return str(n[0])

    #initialize res
    res = "" 

    for i in range(len(n)):
        isFirst = i == 0
        isLast = i == len(n)-1
        isEven = int(n[i]) % 2 == 0
        
        if isFirst:
            if isEven:
                res+=n[i]
            else:
                res+=f"{n[i]}-"
            continue
        
        hasTrailingHypen = res[-1] == "-"

        if isLast:
            if not isEven and not hasTrailingHypen:
                res+=f"-{n[i]}"
                continue
            res+=n[i]
            continue

        if isEven:
            res+=n[i]
        else:
            if hasTrailingHypen:
                res+=f"{n[i]}-"
            else:
                res+=f"-{n[i]}-"

    return res

