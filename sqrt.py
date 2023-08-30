def sqrt(n):
    l = 0
    r = (n // 2) + (n // 2) // 2

    while l <= r:
        mid = (l + r) // 2
        if mid * mid == n:
            print(mid)
            return
        res = mid * mid
        if res > n:
            r = mid - 1
        else:
            l = mid + 1
    # truncated ????
    print(r)
    return r


sqrt(8)
