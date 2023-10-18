class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fac(x):
            result = 1
            while x > 0:
                result *= x
                x -= 1
            return result
        
        return fac(n+m -2) //(fac(m-1) * fac(n-1))
