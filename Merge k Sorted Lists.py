class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        for linked_list in lists:
            curr = linked_list
            while curr:
                heappush(heap, curr.val)
                curr = curr.next

        curr = dummy
        while heap:
            curr.next = ListNode(heappop(heap))
            curr = curr.next
        
        return dummy.next
        
