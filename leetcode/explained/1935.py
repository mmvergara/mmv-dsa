def canBeTypedWords(self, text, brokenletters):
    st = set(brokenletters)
    count = 0
    for strr in text.split(" "):
        add = 1
        for s in st:
            if s in strr:
                add = 0
                break
        count += add

    return count


print(canBeTypedWords("", "leet code", "ld"))
