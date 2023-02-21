class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(), ListNode()
        evenHead = even
        isodd = True
        curr = head

        while curr:
            if isodd:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            isodd = not isodd
            curr = curr.next
        
        even.next = None
        odd.next = evenHead.next

        return head
