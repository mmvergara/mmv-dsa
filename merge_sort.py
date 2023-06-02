def merge(arr:list,start:int,mid:int,end:int):
  # build temp arr to avoid modifying the orignal arr
  arrTemp = []
  i = start
  j = mid + 1

  # while both sub-array have values, then try and merge them in sorted order
  while i <= mid and j <= end:
    if arr[i] <= arr[j]:
      arrTemp.append(arr[i])
      i+=1
    else:
      arrTemp.append(arr[j])
      j+=1
  print(arrTemp)
  return arrTemp
def merge_sort(arr:list,start:int,end:int):
  # Base Case
  if (start < end):
    mid = (start + end) / 2
    merge_sort(arr,start,mid)
    merge_sort(arr,mid+1,end)
    merge_sort(arr,)

  pass

