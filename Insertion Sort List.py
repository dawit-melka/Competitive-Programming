class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5002, head)
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        curr_prev = dummy
        for i in range(n+1):
            if not curr_prev or not curr_prev.next:
                break
            curr = curr_prev.next
            curr_prev.next = curr_prev.next.next
            curr.next = None
            temp = dummy
            for j in range(i+1):
                if j == i or temp.next.val >= curr.val:
                    temp1 = temp.next
                    temp.next = curr
                    curr.next = temp1
                    break
                temp = temp.next

            temp = dummy 
            for _ in range(i+1):
                temp = temp.next
            curr_prev = temp

        return dummy.next
