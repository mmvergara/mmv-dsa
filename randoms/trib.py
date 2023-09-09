def trib(n, mp={}):
    if n in mp:
        return mp[n]
    if n <= 1:
        return 0
    if n == 2:
        return 1

    mp[n] = trib(n - 1) + trib(n - 2) + trib(n - 3)
    return mp[n]


print(trib(5))
