class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        
        def multiply(a, b, m):
            return ((a%m)*b%m)%m
        
        def calcPow(base, exponent, mod):
            result = 1
            while exponent > 0:
                if exponent & 1:
                    result = multiply(base, result, mod)
                base = multiply(base, base, mod)
                exponent >>= 1
            return result
        
        evenPossibilities = calcPow(4, n//2, mod)
        oddPossibilities = calcPow(5, ceil(n/2), mod)
        
        return evenPossibilities * oddPossibilities % mod
        
