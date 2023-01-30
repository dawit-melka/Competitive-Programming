class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return None
        nodes_lessx = []
        nodes_greaterx = []
        
        while head:
            if head.val < x:
                nodes_lessx.append(head)
            else:
                nodes_greaterx.append(head)
            head = head.next

        nodes = nodes_lessx + nodes_greaterx
        for i in range(1,len(nodes)):
            nodes[i-1].next = nodes[i]
        nodes[-1].next = None

        return nodes[0]
