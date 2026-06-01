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
#Two-Pointer Gap -> we make a constant boundary through fast pointer
# Time Complexity - 0(n) runtime due to single pass and Sc- O(1) RAM koi extra array/map nhi
# Dummy node saves head deletion ka crash two pointer se spacing bani rheti

# if Front Deletion- back deletion me list end nhi pata isiliye do pointers ka gap need but here we know starting point is head se sidha n-1 kadam aage ex- delete 3rd so 3-1 means 2 pe khade
# Cycle - find cycle length then cut (pehle cycle detection algo se loop ka end point freeze then usi ko tail maan kr original gap logic )

