class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        temp = head
        def reverseList(node):
            curr, prev = node, None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        maxSum = 0
        halfListHead = reverseList(slow)

        while halfListHead:
            currSum = halfListHead.val + head.val
            maxSum = max(maxSum, currSum)
            halfListHead = halfListHead.next
            head = head.next

        return maxSum
