def countingValleys(steps, path):
    if steps == 0:
        return 0
    l = 0
    arr = []
    valleys = 0
    for x in path:
        if x == "U":
            l+=1
        else:
            l-=1
        if l == 0 and arr[-1] < 0:
            valleys+=1
        arr.append(l)
    return valleys



countingValleys(10,"UDUUUDUDDD")
