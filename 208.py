class Trie:
    def __init__(self):
        self.childrens = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for s in word:
            if s not in node.childrens:
                node.childrens[s] = Trie()
            node = node.childrens[s]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for s in word:
            if s not in node.childrens:
                return False
            node = node.childrens[s]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for s in prefix:
            if s not in node.childrens:
                return False
            node = node.childrens[s]

        return node.is_end or len(node.childrens) > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
