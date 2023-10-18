class Solution:
    def calcPow(self, base, exponent):
        result = 1
        while exponent > 0:
            if exponent & 1:
                result *= base
            base *= base
            exponent >>= 1
        return result
          
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n *= -1
            x = 1 / x
        return self.calcPow(x,n)
