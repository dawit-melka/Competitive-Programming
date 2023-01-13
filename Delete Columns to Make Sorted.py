class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ROWS = len(strs)
        COLS = len(strs[0])
        count = 0

        for c in range(COLS):
            for r in range(1, ROWS):
                if strs[r][c] < strs[r-1][c]:
                    count += 1
                    break 

        return count
