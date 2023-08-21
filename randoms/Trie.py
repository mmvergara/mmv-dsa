class Trie:
    def __init__(self):
        self.childrens = {}
        self.is_end = False

    def insert(self, sq):
        node = self
        for s in sq:
            if s not in node.childrens:
                node.childrens[s] = Trie()
            node = node.childrens[s]
        node.is_end = True

    def query(self, sq):
        res = []
        node = self
        # travel through the Trie
        for s in sq:
            if s not in node.childrens:
                return []
            node = node.childrens[s]

        def rec(node: Trie, curS):
            if node.is_end:
                res.append(curS[:])
            for ch, cn in node.childrens.items():
                rec(cn, curS + ch)

        rec(node, sq)
        return res

    def search(self, sq):
        node = self
        # travel through the Trie
        for s in sq:
            if s not in node.childrens:
                return False
            node = node.childrens[s]
        return node.is_end

    def delete(self, sq):
        def rec(node: Trie, s: str, i: int):
            if i == len(s):
                node.is_end = False
                return len(node.childrens) == 0
            else:
                next_deletion = rec(node.childrens[s[i]], s, i + 1)
                if next_deletion:
                    del node.childrens[s[i]]
                return (
                    next_deletion and not node.is_end and not len(node.childrens) == 0
                )

        rec(self, sq, 0)
        pass

    def __repr__(self) -> str:
        return f"{{ is_end: {self.is_end} , childrens : {self.childrens}}}"


t = Trie()

t.insert("a")
t.insert("abtec")
t.insert("astgc")
t.insert("zz")
t.delete("zz")
print(t.search("zz"))
