
def isHappy(self, n: int) -> bool:
        while n > 9: 
            newN = 0
            x = n
            while x > 9:
                newN += (x % 10)**2
                x = x // 10
            n = newN
        return n


isHappy("",19)
