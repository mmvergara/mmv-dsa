def scramble(s1, s2):
    mp = {}

    for s in s1:
        if s in mp:
            mp[s] += 1
        else:
            mp[s] = 1

    for s in s2:
        if s not in mp or mp[s] == 0:
            return False
        mp[s] -= 1

    return True
