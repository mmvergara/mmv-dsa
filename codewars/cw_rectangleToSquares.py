def sq_in_rect(lng, wdth):
    res = []

    def cut(l,w):
        if l <= 0 or w <= 0:
            return

        l = max(l,w)
        w = min(l,w)
        
        res.append(w)

        cut(l-w,w//w)
        

    cut(lng,wdth)
    return res 


print(sq_in_rect(5,3))
