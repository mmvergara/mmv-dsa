from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"[ val: {self.val}, next: {self.next}]"

# traverse through the linked list, and then the node being traversed will always be the new tail in the new linkedlist
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        while head != None:
            last_head = new_head
            new_head = ListNode(head.val)
            new_head.next = last_head
            head = head.next
        return new_head
            
