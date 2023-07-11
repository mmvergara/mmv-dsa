
def migratoryBirds(arr):
    mp = {}
    f = [0] * 6
    for n in arr:
        f[n]+=1

    maxf = 0
    for i in range(len(f)): 
        if f[maxf] < f[i]:
            maxf = i
    return []



    # Write your code here

res = migratoryBirds([1,2,3,4,5,4,3,2,1,3,4])
print(res)
