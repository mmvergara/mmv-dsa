# adding binary numbers you should know the rules of the adding

# if you add 1 and the res == 3 then carry == 1 and num should be 1
# if you add 1 and the res == 2 then carry == 1 and num should be 0
# if you add 1 and the res == 1 then carry == 0 and num should be 1

def addBinary(self, a: str, b: str) -> str:
    al = len(a) - 1
    bl = len(b) - 1
    a = a[::-1]
    b = b[::-1]
    i = 0
    carry = 0
    out = ""
    while i <= al or i <= bl:
        if i > bl:
            b += "0"
        if i > al:
            a += "0"
        total = int(a[i]) + int(b[i]) + carry
        to_add = "0"
        if total == 1:
            to_add = "1"
            carry = 0

        if total > 1:
            carry = 1
        if total == 3:
            to_add = "1"
        out = to_add + out
        i+=1
    if carry == 1:
        out = "1" + out
    return out


print(addBinary("", "1010", "1001"))
# 10011
