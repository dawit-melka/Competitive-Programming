class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse_ (left, right):
            if left >= right:
                return 
            s[left], s[right] = s[right], s[left]
            reverse_(left+1, right-1)
            
        reverse_(0, len(s)-1)
