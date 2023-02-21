class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        def flip(i1, i2):
            while i1 < i2:
                nodes[i1], nodes[i2] = nodes[i2], nodes[i1]
                i1 += 1
                i2 -= 1

        n = len(nodes)
        k = k % n
        flip(0, n - 1)
        flip(0, k - 1)
        flip(k, n - 1)
        nodes.append(None)

        for i in range(n):
            nodes[i].next = nodes[i+1]
        
        return nodes[0]
