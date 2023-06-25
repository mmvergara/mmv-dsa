
# This is a stack problem where everytime we encounter an operator we pop the last two items on the stack and apply the operator to them and add the result to the stack

def evalRPN(self, tokens: list[str]) -> int:
    operators = ["+","-","*","/"]
    
    stack = []
    def pushAndProcess(val):
        res = val
        if val in operators:
      
            v1 = int(stack.pop())
            v2 = int(stack.pop())
            if val == "+":
                res = v2 + v1
            elif val == "-":
                res = v2 - v1
            elif val == "*":
                res = v2 * v1
            else:
                res = v2 / v1
        stack.append(res)

    [pushAndProcess(x) for x in tokens]


    return stack[0]






res = evalRPN("",["4","13","5","/","+"])
print(res)





