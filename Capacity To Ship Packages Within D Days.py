class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights)-1, sum(weights)+1
        res = r

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days

        while r > l + 1:
            cap = (l + r) // 2
            if canShip(cap):
                r = cap
            else:
                l = cap
        
        return r
