from typing import Optional, List

List = List
Optional = Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{{val:{self.val} , next:{self.next}}}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{{val:{self.val} , left:{self.left} , right:{self.right} }}"

