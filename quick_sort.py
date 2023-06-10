def partition(arr:list,left:int,right:int):
    pivot = arr[right] 
    i =  left - 1

    for j in range(left, right):
        if pivot >= arr[j]:
            i+=1
            arr[i],arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1


def quicksort(arr:int,left:int=0,right=None):
    if right is None:
        right = len(arr)-1

    if left < right:
        new_pivot = partition(arr,left,right)
        quicksort(arr,left,new_pivot-1)
        quicksort(arr,new_pivot+1,right)



arr = [2,3,1,41,4,15,1]

quicksort(arr)

print(arr)




