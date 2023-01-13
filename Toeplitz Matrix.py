class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        for r in range(ROWS-1):
            for c in range(1, COLS):
                if matrix[r+1][c] != matrix[r][c-1]:
                    return False
        
        return True
