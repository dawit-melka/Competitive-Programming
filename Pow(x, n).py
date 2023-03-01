class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        
        def calculate(x, n):
            if n == 0:
                return 1
            if n%2:
                return x * calculate(x, n-1)
            else:
                val = calculate(x, n//2)
                return val*val
        if n < 0:
            x = 1 / x
        return calculate(x, abs(n))
