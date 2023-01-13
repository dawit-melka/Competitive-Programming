class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS*COLS - 1

        while left <= right:
            mid = (left + right)//2
            r = mid//COLS
            c = mid%COLS

            if target > matrix[r][c]:
                left = mid+1
            elif target < matrix[r][c]:
                right = mid-1
            else:
                return True

        return False
