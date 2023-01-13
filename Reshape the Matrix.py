class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        if ROWS * COLS != r * c:
            return mat
        
        newMat = [[] for _ in range(r)]
        currRow = 0
        for row in range(ROWS):
            for col in range(COLS):
                newMat[currRow].append(mat[row][col])
                if len(newMat[currRow]) == c:
                    currRow += 1 
        
        return newMat 
