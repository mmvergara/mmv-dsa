class Fraction():
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def greatest_common_factor(self,num1,num2) -> int:
      if(num1 > num2):
        num1,num2 = num2,num1
      while num1%num2 != 0:
        remainder = num2%num1
        old_num1 = num1
        num1 = remainder
        num2 = old_num1
      return num2

    def __str__(self):
        return f"my top is {self.num} and my bottom is {self.den}"
    
    def __add__(self,otherFraction):
        newnum =self.num * otherFraction.den + self.den * otherFraction.num
        newden = otherFraction.den * self.den

        return Fraction(newnum,newden)
    
    def lowestForm(self):
       gcd = self.greatest_common_factor(self.num,self.den)
       self.num = int(self.num/gcd)
       self.den = int(self.den/gcd)
       return self



myFract = Fraction(4,8)
myFract.lowestForm()
print(myFract)

# myFrac = Fraction(1,2)
# print(myFrac)
# myFrac2 = Fraction(3,4)
# print(myFrac + myFrac2)

