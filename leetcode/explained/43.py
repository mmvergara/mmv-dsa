from collections import deque


# grade school multiplication
def multiply(self, num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return 0
    res = []
    num1 = num1[::-1]
    num2 = num2[::-1]

    print(num1, num2)
    for i in range(len(num1)):
        x = 10**i
        carry = 0
        n1 = int(num1[i])
        iterAns = deque()
        for j in range(len(num2)):
            n2 = int(num2[j])
            prod = n1 * n2 + carry

            # if has carry
            if prod > 9:
                iterAns.appendleft(str(prod % 10))
                carry = (prod // 10) % 10
            else:
                iterAns.appendleft(str(prod))
                carry = 0
        if carry != 0:
            iterAns.appendleft(str(carry))
            carry = 0

        res.append(int("".join(iterAns)) * x)

    return str(sum(res))


multiply("", "123", "456")
