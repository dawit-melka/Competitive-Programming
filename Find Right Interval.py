class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        pairs = []

        for i in range(n):
            pairs.append((intervals[i][0], intervals[i][1], i))

        pairs.sort()
        res = [-1]*n
        for i in range(n):
            currEnd = intervals[i][1]
            left = -1
            right = n
            while right > left + 1:
                mid = (left + right) // 2
                if pairs[mid][0] >= currEnd:
                    right = mid
                else:
                    left = mid
            if right == n:
                continue
            
            res[i] = pairs[right][2]
             
        return res
