
def insertionSort(arr):
    for i in range(1,len(arr)):
        displace = 0
        while i-1-displace >= 0 and arr[i-displace] < arr[i-1-displace]:
            print("swapping")
            arr[i-displace],arr[i-1-displace] = arr[i-1-displace],arr[i-displace]
            displace+=1
    print(arr)



insertionSort([3,4,1,2,23,3])
        













