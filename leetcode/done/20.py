def isValid(self, s: str):
    stack = []
    paren_dict = { ")":"(",  "}":"{",  "]":"["}
    for p in s:
        if len(stack) == 0:
            if p in paren_dict:
                return False
            stack.append(p)
            continue
        
        # if it is a opening
        if p in paren_dict.values():
            print(f"11 appending {p} ")
            stack.append(p)
            continue
        
        # if it is a closing
        if paren_dict[p] == stack[-1]:
            stack.pop()
            continue
        return False
    if len(stack) != 0:
        return False
    return True


paren_dict = {"(": ")", "{": "}", "[": "]"}


print(isValid("","()[]{}"))
print(isValid("","()]"))