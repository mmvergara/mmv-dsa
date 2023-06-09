<<<<<<< HEAD
arr = [1,2,3,4,5]
target = 9


# def twoSum(arr:list,target:int):
#     keepLoop = True
#     for n in arr:
#         if not keepLoop:
#             break
#         for x in arr:
#             if n+x == target:
#                 print("found it ")
#                 keepLoop = False
#                 break

def twoSum(arr:list,target:int):
    complements = {}
    for i,n in enumerate(arr):
        complement = target - n
        print(complements)
        if complement in complements:
            return [i,complements[complement]]
        complements[n] = i
    print("NOT FOUND")

print(twoSum(arr,target))
=======
print(list(range(10,-1,-1)))
>>>>>>> c23f4a06d015f5ddcdae4efdd0544cf6e2343938
