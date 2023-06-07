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
