# DONE
def dailyTemperatures(self, temps: list[int]) -> list[int]:
    stack = [] # [](val,index)
    out = [0] * len(temps)
    
    for i in range(len(temps)):
        while stack and temps[i] >= stack[-1][0]:
            sv,si = stack.pop()
            out[si] = abs(i - si)
        stack.append((temps[i],i))
    print(out)




        


dailyTemperatures("",[73,74,75,71,69,72,76,73])
