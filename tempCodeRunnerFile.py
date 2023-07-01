def rotateLeft(d, arr):
    d = d % len(arr)
    print(d)

    return [*arr[d:] ,*arr[:d]]
    pass
    
    # Write your code here





res = rotateLeft(1,[1,2,3,4,5])
print(res)