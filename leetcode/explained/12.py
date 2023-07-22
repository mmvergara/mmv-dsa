def intToRoman(self, num: int) -> str:
    num = str(num)
    numArr = []

    romans = {
        1: [(5, "V"), (1, "I")],
        2: [(50, "L"), (10, "X")],
        3: [(500, "D"), (100, "C")],
        4: [(1000, "M")],
    }

    count49 = {
        "4": {1: "IV", 2: "XL", 3: "CD"},
        "9": {1: "IX", 2: "XC", 3: "CM"},
    }
    res = ""
    for i in range(len(num)):
        zeroes = "0" * (len(num) - 1 - i)
        numArr.append(f"{num[i]}{zeroes}")

    print(numArr)

    for n in numArr:
        nlen = len(n)
        if n[0] == "0":
            continue

        if n[0] in count49:
            res += count49[n[0]][len(n)]
            continue

        if nlen == 4:
            res += "M" * int(n[0])
            continue

        n = int(n)

        while n != 0:
            i = 0
            if n < romans[nlen][i][0]:
                i += 1
            n -= romans[nlen][i][0]
            res += romans[nlen][i][1]

    return res


res = intToRoman("", 3)
# res = intToRoman("", 58)
res = intToRoman("", 1994)
print(res)
# print(res1)
# print(res2)
