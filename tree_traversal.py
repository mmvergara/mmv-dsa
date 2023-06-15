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

def pre_order_traversal_rec(root):
    out = [root.val]

    def dfspot(left,right):
        if left is not None:
            out.append(left.val)
            dfspot(left.left,left.right)
        if right is not None:
            out.append(right.val)
            dfspot(right.left,right.right)
    dfspot(root.left,root.right)
    return out


# print(pre_order_traversal_rec(root))

def pre_order_traversal_ite(root):
    if root is None:
        return []

    stack = []
    out = []
    node = root

    while stack or node:
        if node:
            out.append(node.val)
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            node = node.right
    return out

# print(pre_order_traversal_ite(root))



def inorder_traversal_rec(root):
    out = []

    def dfspot(node):
        if node is None:
            return

        if node.left is not None:
            dfspot(node.left)

        out.append(node.val)

        if node.right is not None:
            dfspot(node.right)
        
    dfspot(root)
    return out

print(inorder_traversal_rec(root))

def inorder_traversal_ite(root):
    out = []
    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            out.append(node.val)
            node = node.right

    return out


#print(inorder_traversal_rec(root))
#print(inorder_traversal_ite(root))


def post_order_traversal_rec(root):
    out = []
    def dfspot(node):
        if node is None:
            return

        if node.left:
            dfspot(node.left)

        if node.right:
            dfspot(node.right)

        out.append(node.val)
    dfspot(root)
    return out

def post_order_traversal_ite(root):
    out = []
    stack = []
    node = root

    # Visit until left               
    # if not left go right, if no right, get val then backtract

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right:
                node = node.right
            else:
                out.append(node.val)

    return out
            

# print(post_order_traversal_ite(root))



