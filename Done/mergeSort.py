def m(a,s,mid,e):
    atemp = []
    sa1s = s
    sa2s = mid+1

    while sa1s <= mid and sa2s <= e:
        if a[sa1s] < a[sa2s]:
            atemp.append(a[sa1s])
            sa1s+=1
        else:
            atemp.append(a[sa2s])
            sa2s+=1

    while sa1s <= mid:
        atemp.append(a[sa1s])
        sa1s+=1

    while sa2s <= e:
        atemp.append(a[sa2s])
        sa2s+=1

    for k in range(len(atemp)):
        a[s+k] = atemp[k]




def ms(a,s=0,e=None):
    if e is None:
        e = len(a) - 1

    if s < e:
        mid = (s+e) // 2
        ms(a,s,mid)
        ms(a,mid+1,e)
        m(a,s,mid,e)

y = [12,3,1,2,3,2]
ms(y)
print(y)
