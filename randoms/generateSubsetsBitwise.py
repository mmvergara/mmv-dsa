def gen(arr):
    n = len(arr)
    res = []

    for i in range(2**n):
        toBin = bin(i)[2:].zfill(n)
        subset = []
        for i in range(len(toBin)):
            if toBin[i] == "1":
                subset.append(arr[i])
        res.append(subset)
    print(res)


gen(
    [
        1,
        2,
        3,
    ]
)
