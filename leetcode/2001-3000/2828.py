from randoms.dsa import *


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False

        strr = ""
        for i in range(len(words)):
            strr += words[i][0]

