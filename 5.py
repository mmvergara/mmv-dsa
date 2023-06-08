# brute force
def longestPalindrome(self, s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    res_start = 0
    res_end = 1

    def check(start: int, end: int):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    breaker = 0
    for i in range(n-1, -1, -1):
        if breaker == 1:
            break
        for j in range(n-1, -1, -1):
            end = j + i
            if end < n:
                if check(j, end):
                    res_start = j
                    res_end = end + 1
                    print(f"{j} to {end} is palindrome = {s[j:end+1]}")
                    breaker = 1
                    break

    return s[res_start:res_end]


print(longestPalindrome("", "ac"))
