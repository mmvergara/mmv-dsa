class Trie:
    def __init__(self):
        self.is_end = False
        self.childrens = {}

    def insert(self, s):
        node = self
        for ch in s:
            if ch not in node.childrens:
                node.childrens[ch] = Trie()
            node = node.childrens[ch]
        node.is_end = True

    def query(self, st):
        node = self
        s = ""
        res = []
        for ch in st:
            if ch in node.childrens:
                node = node.childrens[ch]

        def rec(node: Trie, curS: str):
            if len(node.childrens) == 0:
                res.append(curS[:])
                return
            elif node.is_end:
                res.append(curS[:])
            for ch, node in node.childrens.items():
                rec(node, curS + ch)
            return

        rec(node, st)
        return res

    def __repr__(self) -> str:
        return f"{{is_end:{self.is_end} , childrens: {self.childrens}}}"


x = Trie()
x.insert("aa")
x.insert("ab")
x.insert("abv")
x.insert("abx")
x.insert("abpca")
x.insert("abpca")
x.insert("abpcasdfa")
x.insert("azzz")
print(x.query(""))
