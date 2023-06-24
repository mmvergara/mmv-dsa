


def birthdayCakeCandles(candles):
    fhash = {}
    cMax = 0
    for n in candles:
        cMax = max(cMax,n)
        if n in fhash:
            fhash[n]+=1
        else:
            fhash[n] = 1p

    return fhash[cMax]



