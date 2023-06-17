
# sort the arr
# loop through array
# with right and left pointer to find which one sums to 0
# left and left-1 should not be equal so we will have unique values

def threeSum(self, nums: list[int]) -> list[list[int]]:
    arr = sorted(nums)

    out = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i + 1
        right = len(arr)-1

        while left < right:
            threeSum = arr[i] + arr[left] + arr[right]

            if threeSum == 0:
                out.append([arr[i],arr[left],arr[right]])
                left+=1
                while arr[left] == arr[left-1] and left < right:
                    left+=1
                continue

            if threeSum > 0:
                right-=1
            else:
                left+=1
    print(out) 
    return out


threeSum("",[0,1,1])
            
        
        

    
