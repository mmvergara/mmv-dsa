arr = [0,2,3,4,1,2,4,5,6]

def insertion_sort(arr):
  arr_out = []
  arrLength = len(arr)
  while(len(arr_out) != arrLength):
    lowestNumIndex = arr.index(min(arr))
    arr_out.append(arr[lowestNumIndex])
    arr.pop(lowestNumIndex)
  return arr_out

print(insertion_sort(arr))
      
         

      