from dsa import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"[ val: {self.val}, next: {self.next}]"

# Is palindrome linked list

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list in-place
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # Step 3: Compare the reversed second half with the first half
        second_half = prev
        first_half = head
        while second_half:
            if second_half.val != first_half.val:
                return False
            second_half = second_half.next
            first_half = first_half.next
        
        return True