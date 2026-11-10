class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Create a dummy node to ease edge cases at the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Ensure there are at least two nodes left to swap
        while prev.next and prev.next.next:
            # Identify nodes to swap
            first = prev.next
            second = prev.next.next
            
            # Rearrange pointers to execute the swap
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev pointer two nodes ahead for the next iteration
            prev = first
            
        return dummy.next
