
def breakingRecords(scores):
    if len(scores) == 0:
        return 0

    cmin = scores[0]
    cmax = scores[0]
    recordBreakMin = 0
    recordBreakMax = 0

    for i in range(1,len(scores)):
        s = scores[i]

        if s < cmin:
            cmin = s
            recordBreakMin+=1

        if s > cmax:
            cmax = s
            recordBreakMax+=1

    return [recordBreakMax,recordBreakMin]
    

