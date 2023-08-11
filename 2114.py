
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mostWords = 0
        for s in sentences:
            if s == "":
                continue
            spaces = 0
            for l in s:
                if l == " ":
                    spaces+=1
            spaces += 1
            mostWords = max(mostWords,spaces)
        return mostWords


