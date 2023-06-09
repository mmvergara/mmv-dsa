def checkIfPalindrome(s:str):
    i = 0 
    j = len(s) - 1

    while i < j:
      if s[i] != s[j]:
          return False
      i+=1
      j-=1
    return True

print(checkIfPalindrome("abba"))
print(checkIfPalindrome("abbba"))
print(checkIfPalindrome("abzba"))
print(checkIfPalindrome("abwwba"))
print(checkIfPalindrome("abbaaz"))