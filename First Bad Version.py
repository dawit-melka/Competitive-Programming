class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n+1

        while high > low + 1:
            mid = (high + low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid
                
        return high
