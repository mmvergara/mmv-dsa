

def first_non_repeating_letter(s:str):
    sArr = s.lower()
    for i,st in enumerate(sArr):
        if sArr.count(st) == 1:
            return s[i]
    return ""

