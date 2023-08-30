def pascal(rows):
    ans = [[1]]
    if rows == 1:
        return ans

    for i in range(rows):
        new = []
        for j in range(-1, len(ans[-1])):
            if j == -1:
                new.append(ans[-1][j + 1])
                continue
            if j + 1 == len(ans[-1]):
                new.append(ans[-1][j])
                continue
            new.append(ans[-1][j] + ans[-1][j + 1])
        ans.append(new)

    for a in ans:
        print(a)


pascal(24)
