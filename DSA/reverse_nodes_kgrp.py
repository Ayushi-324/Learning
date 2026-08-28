class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1: return head
        
        dummy = ListNode(0, head)
        group_prev = dummy 
        
        while True:
            #Check kr k nodes hain ya nahi
            kth = self.getKthNode(group_prev, k)
            if not kth: break 
                
            group_next = kth.next 
            
            #In-place loop chalao aur ulta karo
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            # 3. Pointers ko sahi jagah jod do
            temp = group_prev.next   
            group_prev.next = kth    
            group_prev = temp        
            
        return dummy.next

    def getKthNode(self, curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
