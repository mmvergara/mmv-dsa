from dsa import *


def maximumNumberOfStringPairs(self, words: List[str]) -> int:
    st = set()
    pairs = 0

    for i in range(len(words)):
        cv = words[i][0] + words[i][1]
        if words[i][0] > words[i][1]:
            cv = words[i][1] + words[i][0]
        if cv in st:
            st.remove(cv)
            pairs += 1
        else:
            st.add(cv)
    print(pairs)
    return pairs


maximumNumberOfStringPairs("", words=["cd", "ac", "dc", "ca", "zz"])
