class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)
        before = dummy

        for i in range(left - 1):
            before = before.next

        curr = before.next
        prev = None

        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        before.next.next = curr
        before.next = prev

        return dummy.next   

SUB LIST IN PLACE REVERSAL , time - O(n) single pass r position tk hi traverse , space - O(1) 
