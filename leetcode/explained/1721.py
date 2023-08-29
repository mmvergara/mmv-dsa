from randoms.dsa import *
def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

    left = head
    right = head

    end_pointer = head
    for _ in range(k-1):
        end_pointer = end_pointer.next
        left = end_pointer

    while end_pointer.next:
        right = right.next
        end_pointer = end_pointer.next

    left.val,right.val = right.val , left.val
    return head

    

