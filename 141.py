from dsa import *

def hasCycle(self, head: Optional[ListNode]) -> bool:
    current = head
    while current:
        if current.val == "done":
            return True
        current.val = "repeat"
        current = current.next
    return False
