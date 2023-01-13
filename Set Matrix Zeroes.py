class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        firstRowZero = False
        firstColZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        firstRowZero = True
                    if c == 0:
                        firstColZero = True
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if firstRowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        
        if firstColZero:
            for r in range(ROWS):
                matrix[r][0] = 0
