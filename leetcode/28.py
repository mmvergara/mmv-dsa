def strStr(self, haystack: str, needle: str) -> int:
      try:
          return haystack.index(needle)
      except:
          return -1
    

res1 = strStr("","mississippi","issi")
print(res1)
