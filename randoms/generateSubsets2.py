def gen(arr):
    curArr = [[]]
    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(curArr)):
            curArr.append(curArr[j] + [arr[i]])
    print(curArr)


gen([1, 2, 3, 4])
