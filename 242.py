# def isAnagram(self, s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     s_sum = 0
#     t_sum = 0
#     i = 0
#     for i in range(len(s)):
#         s_sum+=ord(s[i])
#         t_sum+=ord(t[i])
#     if s_sum == t_sum:
#         return True
#     return False
      

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_chars = {}
    t_chars = {}

    for i in range(len(s)):
        if s[i] not in s_chars:
            s_chars[s[i]] = 1
        else:
            s_chars[s[i]] += 1
        
        if t[i] not in t_chars:
            t_chars[t[i]] = 1
        else:
            t_chars[t[i]] += 1
    # assuming 0(1) in getting the size of the map
    if len(s_chars) != len(s_chars):
        return False
    
    for k,v in s_chars.items():
        if t_chars[k] != v:
          return False
        
    return True


isAnagram("","yoyo","yoyo")
        

        
          
        