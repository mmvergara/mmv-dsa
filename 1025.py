
def divisorGame(self, n: int) -> bool:
    aliceTurn = False

    while n != 0 and n!= 1:
        i = 0
        less = None
        while less != 0:
            less = n%(n-i)
            i+=1
        n = n - (n-i+1)
        aliceTurn = not aliceTurn
    print(aliceTurn)
    return aliceTurn
    


divisorGame("",4)

n = 15
mod = 14
# print(10-(n%mod))
