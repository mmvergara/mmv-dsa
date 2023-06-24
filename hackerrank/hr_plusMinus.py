
def plusMinus(arr):
    n = len(arr)
    values = [0]*3

    for i in range(len(arr)):
        if arr[i] > 0:
            values[0]+=1
        elif arr[i] < 0:
            values[1]+=1
        else:
            values[2]+=1

    for i in range(len(values)):
        values[i] = values[i] / n
        print(values[i])




