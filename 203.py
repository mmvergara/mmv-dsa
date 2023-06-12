from dsa import *


def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

    # handle the case where the head has the value
    while head and head.val == val:
        head = head.next

    prev = head
    curr = head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = current.next
    return head
    

print(ListNode(1))
