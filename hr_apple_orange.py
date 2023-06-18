
def countApplesAndOranges(s, t, a, b, apples, oranges):

    totalA = 0
    totalB = 0

    def inRange(x):
        return x >= s and x <= t


    for i in range(len(apples)):
        x = apples[i]+a
        if inRange(x):
            totalA+=1
        
    for i in range(len(oranges)):
        x = oranges[i]+b
        if inRange(x):
            totalB+=1
            



    print(totalA)
    print(totalB)


