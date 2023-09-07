def reverseVowels(self, s: str) -> str:
    vowels = set(["a", "A", "E", "e", "I", "i", "O", "o", "U", "u"])
    vowIdx = []
    listS = list(s)
    for i in range(len(listS)):
        if s[i] in vowels:
            vowIdx.append(i)

    for i in range(len(vowIdx)):
        print(vowIdx[i])
        listS[vowIdx[i]] = s[vowIdx[len(vowIdx) - i - 1]]
    return "".join(listS)


reverseVowels("", "heilo")
