from dsa import *

# 1234 ll
ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))


def swap(beforel1: Optional[ListNode], l1: Optional[ListNode], l2: Optional[ListNode]):
    lastTail = l2.next
    
    if beforel1 is not None:
        beforel1.next = l2
    else:
        l1 = l2

    l2.next = l1
    l1.next = lastTail


def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    swap(None, head, head.next)
    print(head)
    pass


swapPairs("", ll)
