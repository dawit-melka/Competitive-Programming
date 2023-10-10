class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        def findPlace(target):
            left = -1
            right = len(heaters)
            
            while right > left + 1:
                mid = (left + right) // 2
                if heaters[mid] >= target:
                    right = mid
                else:
                    left = mid
            
            return (left, right)
        
        result = -1
        for house in houses:
            l, r = findPlace(house)
            if l == -1:
                result = max(result, abs(house - heaters[r]))
            elif r == len(heaters):
                result = max(result, abs(house - heaters[l]))
            else:
                result = max(result, min(abs(house - heaters[l]), abs(house - heaters[r])))
        
        return result
