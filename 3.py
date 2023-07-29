def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    maxL = 0
    mp = {}
    l = 0

    for right in range(n):
        if s[right] in mp and mp[s[right]] >= l:
            l = mp[s[right]] + 1
        mp[s[right]] = right
        maxL = max(maxL, right - l + 1)
    print(maxL)
    return maxL


lengthOfLongestSubstring("", "abba")
