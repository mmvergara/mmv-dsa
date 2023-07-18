def rev(s):
    if len(s) == 1:
        return s

    return s[-1] + rev(s[:-1])


print(rev("yowwqeq"))
