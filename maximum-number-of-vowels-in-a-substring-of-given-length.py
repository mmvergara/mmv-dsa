def maxVowels(self, s: str, k: int) -> int:
    vowels = ["a","e","i","o","u"]
    maximumVowels = 0
    for i in range(len(s)):
        if (i + k) > len(s):
            break
        curString = s[i]
        for j in range(i+1,k+i):
            curString+=s[j]
        maximumVowels = max(maximumVowels,sum([1 if s in vowels else 0 for s in curString]))
    return maximumVowels

print(maxVowels("","abciiidef",3))