def merge(arr: list, start: int, mid: int, end: int):
    arrTemp = []
    subArr1Start = start
    subArr2Start = mid + 1

    while subArr1Start <= mid and subArr2Start <= end:
        if arr[subArr1Start] <= arr[subArr2Start]:
            arrTemp.append(arr[subArr1Start])
            subArr1Start += 1
        else:
            arrTemp.append(arr[subArr2Start])
            subArr2Start += 1

    while subArr1Start <= mid:
        arrTemp.append(arr[subArr1Start])
        subArr1Start += 1

    while subArr2Start <= end:
        arrTemp.append(arr[subArr2Start])
        subArr2Start += 1

    for k in range(len(arrTemp)):
        arr[start + k] = arrTemp[k]


def merge_sort(arr: list, start: int = 0, end: int = None):
    if end == None:
        end = len(arr) - 1

    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


arr = [2, 3, 1, 2, 5, 6, 2]
merge_sort(arr)
print(arr)
