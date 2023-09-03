# We need to remove the spaces first.
import re
def isPalindrome(self, s: str) -> bool:
    s = re.sub(r'[\W_]', '', s).lower()
    print(s)
    l = 0
    r = len(s) - 1
    while r >= l:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True