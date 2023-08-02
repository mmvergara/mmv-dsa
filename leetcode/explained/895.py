def buddyStrings(self, s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    diffs = []

    dups = False
    st = set()

    for i in range(len(s)):
        if s[i] != goal[i]:
            diffs.append(i)
        if not dups and s[i] in st:
            dups = True
        st.add(s[i])

    if len(diffs) == 2:
        mp1 = set()
        mp2 = set()
        for i in diffs:
            mp1.add(s[i])
            mp2.add(goal[i])
        print(f"returning {mp1 == mp2}")
        return mp1 == mp2
    if dups and len(diffs) == 0:
        return True
    else:
        return False

    # base case if there are dups


buddyStrings("", "abcaa", "abcbb")
