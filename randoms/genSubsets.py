def gen(arr:list):
    res = [[]]

    def g(index,arrC):

        for i in range(index,len(arr)):
            arrC.append(arr[i])

            res.append(arrC.copy())

            g(i+1,arrC.copy())

            arrC.pop()
            
    g(0,[])

    print(res)
    return res





gen([1,2,3])
