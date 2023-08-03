def perms(n, choices: list):
    res = []

    def rec(arr):
        nonlocal choices
        nonlocal n
        nonlocal res
        if len(arr) == n:
            res.append(arr)
            return

        for c in choices:
            rec(arr[:] + [c])

    rec([])
    print(res)
    pass


perms(3, ["R", "G", "B", "O"])
