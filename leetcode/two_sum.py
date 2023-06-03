arr = [2,7,14,19]
target = 9

def two_sum(arr:list,target:int) -> tuple:
    arrMap = {}
    for i in range(len(arr)):
        print(arr[i])
        complement = target - arr[i]
        print(complement)
        if(complement in arrMap):
            return [arrMap[complement],i]
        else:
            arrMap[arr[i]] = i
            print(arrMap)
    return [None,None]
    
print(two_sum(arr,target))


