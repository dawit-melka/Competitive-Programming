class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ahead_node = head

        while n:
            ahead_node = ahead_node.next
            n -= 1
        
        delay_node = dummy
        while ahead_node:
            ahead_node = ahead_node.next
            delay_node = delay_node.next
        
        delay_node.next = delay_node.next.next

        return dummy.next
