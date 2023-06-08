import sys
def firstUniqChar(self, s: str) -> int:
    characters = {}
    for i,c in enumerate(s):
        if c not in characters:
            characters[c] = i
            continue
        if characters[c] != -1:
            characters[c] = -1
    min_index = sys.maxsize
    for i in characters.values():
        if i < min_index and i >= 0:
            min_index = min(min_index,i)
    if min_index == sys.maxsize:
        min_index = -1
    return min_index
          

print(firstUniqChar("","leetcode")) 
# leetcode
# characters = { "l" : i }
        