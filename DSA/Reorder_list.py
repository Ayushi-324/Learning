class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next:
            return None

        slow = fast = head
        while fast and fast.next:  #slow 1 step fast 2 step (slow at middle and fast end pe hoga)
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next  #ques 206 wala logic reverse linked list 
            curr.next = prev
            prev = curr
            curr = nxt

        first = head
        second = prev

        while second:
            tmp1 = first.next  # 1-> 5 se
            tmp2 = second.next  # 5 -> 2

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


# AT first the intution was that just take whatever u want and do .next but it's singly linked list jisko bs aage ka rasta pata hai aur agar har bar last node tak jana hua toh bar bar traverse takes O(n2)
# PATTERN - 1. Find middle 2. Reverse second half 3. Merge both halves
# ARRAY use ho skta tha thatll ke sare element arr me dale  then using two pointer approach ek pointer start me ek end me and nodes link kr do  but takes O(N) extra space and ll takes O(1)
# Time  : O(N), Space : O(1) keval nodes rearrange kr rhe h
