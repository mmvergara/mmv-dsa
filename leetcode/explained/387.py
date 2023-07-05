import sys

# loop through the string while counting the frequency

def firstUniqChar(self, s: str) -> int: # returns the index of the firstUniqChar
    # Create a hashmap of characters with their index
    characters = {}

    # loop through the string
    for i,c in enumerate(s):
        
        # If we first encounter the letter 
        if c not in characters:
            characters[c] = i
            continue

        # if we already encountered the letter make it -1
        if characters[c] != -1:
            characters[c] = -1


    min_index = sys.maxsize
    # loop through the character values and find the lowest index (lowest index means is the first letter that is unique because we eleminated all repeating characters in line 17-19)

    for i in characters.values():
        if i < min_index and i >= 0:
            min_index = min(min_index,i)

    # edge cases
    if min_index == sys.maxsize:
        min_index = -1
    return min_index
          

print(firstUniqChar("","leetcode")) 
# leetcode
# characters = { "l" : i }
        