class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split(" ")
        return " ".join([arr[i] for i in range(k)])
