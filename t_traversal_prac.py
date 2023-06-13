from dsa import *


# Create the nodes
root = TreeNode("A")
node2 = TreeNode("B")
node3 = TreeNode("C")
node4 = TreeNode("D")
node5 = TreeNode("E")
node6 = TreeNode("F")

# Set the relationships between the nodes
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

#         A
#       /   \
#      B     C
#     / \   /
#    D  E  F


def pre_order(root):
    out = []

    def dfspot(root):
        if root is None:
            return
        out.append(root.val)

        if root.left:
            dfspot(root.left)
        if root.right:
            dfspot(root.right)
    dfspot(root)
    return out

# print(pre_order(root))


def pre_order_ite(root):

    out = []
    stack = [root]

    while stack:
        node = stack.pop()
        out.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
            
    return out

# print(pre_order_ite(root))
        



def in_order_rec(root):
    if root is None:
        return []

    out = []

    def dfspot(node):
        if node is None:
            return

        if node.left:
            dfspot(node.left)

        out.append(node.val)

        if node.right:
            dfspot(node.right)

    dfspot(root)
    ret



print(in_order_ite(root))






    



