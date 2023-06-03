def twosum(arr:list,target:int):
    complementsDict = {}
    for i in range(len(arr)):
        complement = target - arr[i] 
        print(complement)
        if complement in complementsDict:
            return [complementsDict[complement],i]
        else:
            complementsDict[arr[i]] = i
        print(complementsDict)
    return None


res = twosum([1,2,6,7,8,9,3,2,1],17)
print(res)
