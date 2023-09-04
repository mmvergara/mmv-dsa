class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clonegraph(self, node):
        mp = {}

        def clone(node):
            if node in mp:
                return mp[node]

            cpy = node(node.val)
            mp[node] = cpy

            for n in node.neighbors:
                cpy.neighbors.append(clone(n))

            return cpy

        return clone(node)
