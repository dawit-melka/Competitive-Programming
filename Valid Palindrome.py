class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            
            while right > left and not s[right].isalnum():
                right -= 1
            
            left_char = s[left]
            right_char = s[right]
            if left_char.isalpha():
                left_char = left_char.lower()
            if right_char.isalpha():
                right_char = right_char.lower()
            
            if left_char != right_char:
                return False
            
            left += 1
            right -= 1

        return True
