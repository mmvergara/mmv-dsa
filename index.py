arr = [1,2,3,34,4]
target = 38

def twosum(arr,target):
    print(arr)
    print(f"target is {target}")
    complements = {}
    
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in complements:
            return [i,complements[complement]]
        complements[arr[i]] = i 
    return None

print(twosum(arr,target))


