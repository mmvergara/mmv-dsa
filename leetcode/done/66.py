# start from the end, then add one, if its == 10 ( only equals because we are only adding one)
# keep tract of the carry variable and you add it as you go on
# if the carry is still == 1 after iterating/adding through all of the numbers
# we insert a 1 in the end of the array
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
