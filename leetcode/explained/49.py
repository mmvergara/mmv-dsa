# Another approach is
# sort the str, if the str matches something in the hashlist, put it in there else put a new one with the array as the first pair
# return the values of the hashlist

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    hashlist = []
    out = []
    for sr in strs:
        sf = {}
        for s in sr:
            if s in sf:
                sf[s] += 1
            else:
                sf[s] = 1
        
        if sf in hashlist:
            i = hashlist.index(sf)
            out[i].append(sr)
        else:
            hashlist.append(sf)
            out.append([sr])

    return out


        
