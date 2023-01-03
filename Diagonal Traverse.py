class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        is_up = True
        res = []
        r, c = 0, 0
        
        while True:
            res.append(mat[r][c])
            
            if r==rows-1 and c==cols-1:
                break
            
            if is_up:
                if r > 0 and c < cols-1:
                    r -=1
                    c += 1
                elif c+1 >= cols:
                    is_up = False
                    r += 1
                else:
                    is_up = False
                    c += 1
            else:
                if r < rows-1 and c > 0:
                    r += 1
                    c -= 1
                elif r+1 >= rows:
                    is_up = True
                    c += 1
                else:
                    is_up = True
                    r += 1

        return res
