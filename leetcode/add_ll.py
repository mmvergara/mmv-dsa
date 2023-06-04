from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = []  # List to store the sum of corresponding digits
        
        # Iterate until both lists reach the end
        while l1 is not None or l2 is not None:
            # If either list reaches the end, replace it with a ListNode(0) to continue the addition
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)

            # Add the values of l1 and l2 and append the sum to total
            total.append(l1.val + l2.val)

            # Move to the next node in l1 and l2 if available, otherwise set to None
            l1 = l1.next if l1.next is not None else None
            l2 = l2.next if l2.next is not None else None

        final_sum = total.copy()  # Create a copy of total to store the final sum
        carry = 0  # Variable to track the carry value

        # Iterate through the total list and adjust the sum and carry values
        for i, n in enumerate(total):
            n = n + carry  # Add the carry value to the current sum

            if n > 9:
                final_sum[i] = int(str(n)[-1])  # Store the last digit of the sum
                carry = 1  # Set carry to 1 for the next iteration
            else:
                final_sum[i] = n  # Store the sum as is
                carry = 0  # Reset the carry value

        if carry == 1:
            final_sum.append(1)  # If a carry remains after the last iteration, add it as a new digit
        
        head = ListNode(final_sum[0])  # Create the head node of the resulting linked list
        current = head

        # Iterate through the final sum list and create the linked list nodes
        for i in range(1, len(final_sum)):
            new_node = ListNode(final_sum[i])
            current.next = new_node
            current = current.next

        return head  # Return the head of the resulting linked list
