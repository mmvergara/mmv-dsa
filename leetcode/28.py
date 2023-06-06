def strStr(self, haystack: str, needle: str) -> int:
    for i in range(0,len(haystack)):
      cur_str = haystack[i:i+len(needle)]
      print(cur_str)
      if cur_str == needle:
         return i
    return -1


res1 = strStr("","mississippi","issi")
print(res1)
