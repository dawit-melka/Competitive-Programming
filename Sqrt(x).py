class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = -1, x+1
        
        while high > low+1:
            mid = (high + low)//2
            if mid*mid > x:
                high = mid
            elif mid*mid < x:
                low = mid
            else:
                return mid

        return low
