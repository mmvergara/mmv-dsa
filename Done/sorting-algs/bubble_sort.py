def bubble_sort(arr:list):
    solved = 0
    while(solved != len(arr)):
      for i in range(len(arr)-solved):
        try:
          if(arr[i] > arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]
        except:
          pass
      solved+=1    
    pass



arr = [2,1,5,2,5,7,8,10]

res = bubble_sort(arr)