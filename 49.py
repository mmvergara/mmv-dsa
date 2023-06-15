
# brute force
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    out = []
    hashlist = []
    for i in range(len(strs)):
        cur_hash = {}
        for s in strs[i]:
            if s in cur_hash:
                cur_hash[s]+= 1
            else:
                cur_hash[s]=1
        if cur_hash not in hashlist:
            hashlist.append(cur_hash)
            out.append([strs[i]])
        else:
            hashIndex = hashlist.index(cur_hash)
            print(f'hash index {hashIndex}')
            out[hashIndex].append(strs[i])
    return out


#sorting method
def groupAnagramsS(self,strs:list[str]):
    dic = {}
    for s in strs:
        sortedWord = "".join(sorted(s))
        if sortedWord in dic:
            dic[sortedWord].append(s)
        else:
            dic[sortedWord] = [s]
    print(dic.values())
    return dic.values()


groupAnagramsS("",["eat","tea","tan","ate","nat","bat"])
