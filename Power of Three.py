class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        return n > 1 and self.isPowerOfThree(n/3)
