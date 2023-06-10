def pt(a,l,h):
    p = a[h]
    i = l - 1
    
    for j in range(l,h):
        if p >= a[j]:
            i+=1
            a[i],a[j] = a[j],a[i]
    
    a[h],a[i+1] = a[i+1], a[h]

    return i + 1

def qs(a,l=0,h=None):
    if h is None:
        h = len(a) - 1

    if l < h:
        p = pt(arr,l,h)
        qs(arr,p+1,h)
        qs(arr,l,p-1)

arr = [2,23,31,22,3,2]
qs(arr)
print(arr)
        
            
