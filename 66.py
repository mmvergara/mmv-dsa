def plusOne(self, digits: list[int]) -> list[int]:
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            digits[i] = 0
        else:
            carry = 0
            break
    if carry == 1:
        digits.insert(0,1)
    return digits


plusOne("", [1, 2, 9])
