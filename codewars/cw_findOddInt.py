
def find_it(seq):
    hset = {}

    for n in seq:
        if n in hset:
            hset[n]+=1
        else:
            hset[n] = 1

    for k,v in hset.items(): 
        if v % 2 != 0: 
            return k
    return None



print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
