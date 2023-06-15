from dsa import *


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    before_left = None
    left = head
    right = head

    for _ in range(n):
        right = right.next

    while right:
        before_left = left
        left = left.next
        right = right.next

    if before_left is None:
        return left.next
    
    before_left.next = left.next
    return head
    

