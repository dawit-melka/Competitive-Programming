class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < n
        for dy in range(-n+1, n):
            for dx in range(-n+1, n):
                currAns = 0
                for r in range(n):
                    if not(0 <= r+dy < n):
                        continue
                    for c in range(n):
                        currR, currC = r + dy, c + dx
                        if inBound(currR, currC):
                            currAns += (img1[currR][currC] * img2[r][c])
                
                ans = max(ans, currAns)
        
        return ans
        
