class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        def findIntersection(meet):
            curr = head
            while curr != meet:
                curr = curr.next
                meet = meet.next
            return meet


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return findIntersection(fast)
        
        return None
