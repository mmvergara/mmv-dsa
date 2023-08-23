from collections import Counter

def longestPalindrome(self, s: str) -> int:
    ans = 0
    sCount = Counter(s).values()
    for v in sCount:
        ans += 5 // 2 * 2
        if ans % 2 == 0 and v % 2 == 1:
            ans+=1
    return ans


longestPalindrome("","abccccdd")
