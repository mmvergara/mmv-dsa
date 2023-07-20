def gen(arr):
    subsets = []

    def rec(arr, curArr, i, pos):
        if len(arr) == len(curArr):
            subsets.append(curArr[:])
            return

        newArr = curArr[:]
        newArr.insert(pos, arr[i])

        for x in range(len(curArr) + 1):
            rec(arr, newArr[:], i + 1, x - 1)

    rec(arr, [], 0, 0)
    return subsets


gen(["A", "B", "C"])
