def isIsomorphic(self, s, t):
    if len(s) != len(t):
        return False
    n = len(s)
    mp = {}
    mpd = set()

    for i in range(n):
        if s[i] in mp:
            if mp[s[i]] != t[i]:
                return False
        else:
            if t[i] in mpd:
                return False
            mpd.add(t[i])
            mp[s[i]] = t[i]
    print(mp)
    return True
