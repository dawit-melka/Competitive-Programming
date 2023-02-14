class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        l, r = 0, len(values) -1
        while l < r:
            if values[l] != values[r]:
                return False
            l += 1
            r -= 1
        return True

            
