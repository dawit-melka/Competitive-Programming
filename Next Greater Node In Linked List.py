class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        index = 0
        stack = []
        curr = head
        n = 0

        while curr:
            curr = curr.next
            n += 1
        
        curr = head
        answer =[0]*n
        while curr:
            while stack and curr.val > stack[-1][0]:
                node, idx = stack.pop()
                answer[idx] = curr.val

            stack.append((curr.val, index))
            index += 1
            curr = curr.next
        
        return answer
