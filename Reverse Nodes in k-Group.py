class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        newHead = None
        kth_node = None
        curr_node = head

        while curr_node:
            k_nodes = []
            count = k
            while count and curr_node:
                k_nodes.append(curr_node)
                curr_node = curr_node.next
                count -= 1

            if len(k_nodes) == k:
                k_nodes.reverse()

            if newHead == None:
                newHead = k_nodes[0]

            for i in range(len(k_nodes)-1):
                k_nodes[i].next = k_nodes[i+1]

            if kth_node != None:
                kth_node.next = k_nodes[0]

            kth_node = k_nodes[-1]
        
        k_nodes[-1].next = None
        return newHead
