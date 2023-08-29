from randoms.dsa import *

# Keep tract of the node before the node to be removed and then move the pointer to the nodeToBeremoved.next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        prev = head
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return head
