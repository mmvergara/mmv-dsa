import random
class MSDIE:
    def __init__(self,sides):
        self.sides = sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value =random.randrange(1,self.sides+1)
        return self.current_value
    
    def __repr__(self) -> str:
        return f"{self.current_value}"

d_list = [MSDIE(5)]
print(d_list)

        
        