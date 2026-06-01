class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  #dummy node to handle head deletion
        dummy.next = head

        slow = dummy  #initialize both pointer at dummy node
        fast = dummy

        for _ in range(n): #create gap of n nodesby moving fast pointer ahead taki slow se n-dist gap bane
            fast = fast.next

        while fast.next is not None: #move both pointers until fast reaches last node so slow shi jgh pahuche
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next #skip target node agle se agle padosi se dosti

        return dummy.next  #return actual new head

# LOGIC - Fast and slow pointers
