def is_valid_walk(walk):
    # it has to be a 10 minutes walk
    if len(walk) != 10:
        return False
    
    f = {'n':0,'s':0,'e':0,'w':0}

    for d in walk:
        f[d]+=1

    if f["n"] != f["s"]:
        return False

    if f["e"] != f["w"]:
        return False

    return True
