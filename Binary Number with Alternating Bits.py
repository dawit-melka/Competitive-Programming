class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prevBit = n & 1
        n = n >> 1

        while n:
            if n & 1 == prevBit:
                return False
            prevBit = n & 1
            n = n >> 1

        return True
