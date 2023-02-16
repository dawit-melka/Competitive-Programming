class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)
        leftPrev, rightNext = dummyHead, None
        count = 0
        curr = dummyHead
        while count < right:
            count += 1
            if count == left:
                leftPrev = curr
            curr = curr.next
        if curr:
            rightNext = curr.next
            curr.next = None
        left = leftPrev.next
        
        def reverseList(node):
            curr = node
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        leftPrev.next = reverseList(left) 
        left.next = rightNext
       
        return dummyHead.next
