import math

def b_search(arr:list,target:int,start=0,end=None):
  print(start,end)
  if end == None:
    end = len(arr) -1

  mid = math.trunc((start+end)/2)
  if arr[mid] == target:
    return mid

  if start == end:
    return False
  
  if target > arr[mid]:
    return b_search(arr,target,mid+1,end)
  else:
    return b_search(arr,target,start,mid-1)
  

sArr = [1,2,3,4,5,6,7,8,9,10]
print(b_search(sArr,61))
