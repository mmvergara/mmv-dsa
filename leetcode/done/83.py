from randoms.dsa import *


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        current = head

        while current.next:
            if current.val == current.next.val:
                print("same val as next")
                current2 = current
                while current2 and current2.val == current.val:
                    current2 = current2.next
                current.next = current2
                continue
            current = current.next
        print(head)

        return head
