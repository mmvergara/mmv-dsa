
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1

    for j in range(low,high):
        if pivot >= arr[j]:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

def qs(arr,low=0,high=None):
    if high is None:
        high = len(arr)-1

    if low < high:
        pivot = partition(arr,low,high)
        qs(arr,pivot+1,high)
        qs(arr,low,pivot-1)



























