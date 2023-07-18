import sys


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{{ val: {self.val}, next: {self.next}}}"


head = Node(1, Node(2, Node(3, Node(4))))


target = 4
change = Node(10)

cur = head
while cur.next.val != target:
    cur = cur.next

change.next = cur.next.next
cur.next = change

print(head)
