class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)  #edge cases -> dummy node to track track head 
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val: #jb tk dono list me values hai compare krte jao
                tail.next = list1
                list1 = list1.next  # so that next value compare ho 
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  #tail ko aage bdhate jana h 

        tail.next = list1 if list1 else list2  #BOUNDARY COND -> agar ek list khatam bachi hui puri list sidha jodo as sorted h 

        return dummy.next  #dummy ka agla dabba hi merge list ka head 

# list already sorted hai just dono list ki values compare krke .next se jodte jana hai 
# TIME COMP-> O(M+N)  or O(n)  as visiting both list once , m n are len of both
# SPACE COMP -> O(1) no new list only in-place sorting 
