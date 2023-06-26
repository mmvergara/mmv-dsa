# Uses monotonic stack
def dailyTemperatures(self, temps: list[int]) -> list[int]:
    
    # initialize stack and the out which is size len(temps)
    stack = [] # [](val,index)
    out = [0] * len(temps)
    
    # loop through temps
    for i in range(len(temps)):

        # monotonic stack nature
        # if there is value in the stack and the current temp is >= than the top of stack
        while stack and temps[i] >= stack[-1][0]:

            # pop the stack and get the values
            sv,si = stack.pop()

            # out[index of the popped value] = days interval of the current day and the day of the popped value
            out[si] = abs(i - si)

        # append to the top of the stack
        stack.append((temps[i],i))
    return out


res = dailyTemperatures("",[73,74,75,71,69,72,76,73])
print(res)
