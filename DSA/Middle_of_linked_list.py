class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize both pointers at the head of the list
        slow = head
        fast = head
        
        # Traverse the list until the fast pointer reaches the end
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
        # When fast reaches the end, slow is exactly at the middle node
        return slow
