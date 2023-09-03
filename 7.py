def reverse(self, x):
    ans = 0
    s = 1
    if x < 0:
        x *= -1
        s = -1

    while x != 0:
        a = x % 10
        ans = ans * 10 + a
        x //= 10
    res = ans * s
    if res > 2147483647:
        return 0
    if res < 2147483648:
        return 0

    return ans * s


reverse("", -123)
