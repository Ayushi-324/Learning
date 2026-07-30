class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node acts as a placeholder for the start of the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Loop continues while lists have nodes or a carry remains
        while l1 or l2 or carry:
            # Extract values, using 0 if a list is already exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for the current position
            total = val1 + val2 + carry
            
            # Compute new carry and the digit to store
            carry = total // 10
            new_digit = total % 10
            
            # Append new digit to the result list
            current.next = ListNode(new_digit)
            current = current.next
            
            # Advance input list pointers if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return the actual head of the new linked list
        return dummy.next
