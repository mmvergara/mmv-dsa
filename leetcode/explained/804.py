from randoms.dsa import *


def uniqueMorseRepresentations(self, words: List[str]) -> int:
    mc = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]
    letter_to_position = {}

    st = set()
    for i in range(26):
        letter = chr(ord("a") + i)
        letter_to_position[letter] = i + 1

    for w in words:
        strr = ""
        for s in w:
            strr += mc[letter_to_position[s] - 1]
        st.add(strr)
    return len(st)


uniqueMorseRepresentations("", words=["gin", "zen", "gig", "msg"])
