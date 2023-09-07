def convert(self, s: str, numRows: int) -> str:
    strs = ["" for _ in range(numRows)]

    asc = True
    i = -1

    for st in s:
        if i <= 0:
            asc = True
        if i == numRows-1:
            asc = False
        if asc:
            i += 1
        else:
            i -= 1
        strs[i]+=st

    print(strs)
    return "".join(strs)


res = convert("", "PAYPALISHIRING", 4)
print(res)
