# two
def twoSumBF(arr:list,target:int):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                print(f"found it {i,j}")
                return [i,j]
    print("NOT FOUND")
    return None

twoSumBF([1,2,3,4,5],9)










