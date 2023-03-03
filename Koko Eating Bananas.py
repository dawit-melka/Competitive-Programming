class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isPosible(bananas):
            count = 0
            for num in piles:
                count += ceil(num/bananas)
                if count > h:
                    return False
            return True

        min_banana = 0
        max_banana = max(piles)+1

        while max_banana > min_banana+1:
            mid = min_banana + (max_banana - min_banana)//2
            if isPosible(mid):
                max_banana = mid
            else:
                min_banana = mid

        return max_banana
