class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        n = 0
        curr, lastNode = head, None

        while curr:
            n += 1
            lastNode = curr
            curr = curr.next

        k %=  n
        if k == 0:
            return head

        curr = head
        gap = n - k-1

        while gap:
            curr = curr.next
            gap -= 1

        newHead = curr.next
        lastNode.next = head
        curr.next = None

        return newHead
