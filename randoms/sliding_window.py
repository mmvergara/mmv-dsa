# Problem
# given an array of integers get maximum sum of numbers of a sub-array lenght of k



def sliding_windows(arr:list[int],k:int):
    current_max = sum([n for n in arr[0:k]])
    new_max = current_max
    for i in range(k,len(arr)):
      new_max = new_max + arr[i] - arr[i-k]
      current_max = max(current_max,new_max)
      print(current_max)
    return current_max

sliding_windows([1,4,5,6,1,2,4,6,8,10,9,10,2],3)





