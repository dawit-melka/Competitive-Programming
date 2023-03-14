class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        def isValid(i):
            l, r = -1, n
            while r > l + 1:
                mid = (l + r) // 2
                if citations[mid] < i:
                    l = mid
                else: r = mid
           
            return n - r >= i

        left , right = -1, n+1

        while right > left + 1:
            mid = (left + right) // 2
            if isValid(mid):
                left = mid
            else: right = mid
            
        return left
