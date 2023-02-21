class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        behind = dummy
        curr = head
        isduplicated = False

        while curr:
            isduplicated = False
            while curr and curr.next and curr.val == curr.next.val:
                curr = curr.next
                isduplicated = True
            
            if isduplicated:
                behind.next = curr.next
            else:
                behind.next = curr
                behind = behind.next
            curr = curr.next

        return dummy.next
