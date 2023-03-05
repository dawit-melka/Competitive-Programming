# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5002, head)
        curr_prev = dummy
        i = 0

        while curr_prev and curr_prev.next:
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
            i += 1

        return dummy.next
        
