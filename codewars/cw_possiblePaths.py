def travel_chessboard(s):
    loc1 = tuple(map(int, s[1:4].split(",")))
    loc2 = tuple(map(int, s[6:9].split(",")))

    print(loc1, loc2)
    m = abs(loc1[0] - loc2[0] + 1) + 1
    n = abs(loc1[1] - loc2[1] + 1) + 1
    print(m, n)


travel_chessboard("(1,8)(4,8)")
travel_chessboard("(1,1)(3,3)")
