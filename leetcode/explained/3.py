# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
        return 0
    subStr = ""
    maxSubStr = 0 
    for i in range(len(s)):
        if subStr == "":
            subStr += s[i]
            maxSubStr+=1
            continue
        if s[i] in subStr:
            subStr = subStr[subStr.rindex(s[i])+1:]
            subStr += s[i]
        else:
            subStr += s[i]
        if maxSubStr < len(subStr):
            print(subStr)
            maxSubStr = len(subStr) 
    return maxSubStr

        

# print(lengthOfLongestSubstring("","abcabcbb")) # 3
print(lengthOfLongestSubstring("","dvdf")) # 3
# print(lengthOfLongestSubstring("","aabaab!bb")) # 1'

# strr = "dvdf"
# print(strr[strr.rindex("d")+1:])