
def diagonalDifference(arr):
    # top-left to bottom-right
    r = 0
    c = 0
    sum1 = 0
    while r < len(arr) and c < len(arr[0]):
        sum1 += arr[r][c]
        r+=1
        c+=1

    # top-right to bottom-left
    r = 0
    c = len(arr[0])-1
    sum2 = 0
    while r < len(arr) and c >= 0:
        sum2 += arr[r][c]
        r+=1
        c-=1
    
    return abs(sum1 - sum2)




res = diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
print(res)
