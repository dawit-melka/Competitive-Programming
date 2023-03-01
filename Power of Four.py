class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1 : return True
        return n > 1 and self.isPowerOfFour(n/4)
