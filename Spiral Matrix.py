class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nextMove = {"right":"down", "down":"left", "left":"up", "up":"right"}
        move = {"right" : [0, 1], "down" : [1, 0], "left" : [0, -1], "up" : [-1, 0]}
        currMove = "right"
        currRow = 0
        currCol = 0
        visited = set()
        res = []
        ROWS = len(matrix)
        COLS = len(matrix[0])

        while (len(res) < ROWS*COLS):
            res.append(matrix[currRow][currCol])
            visited.add((currRow, currCol))
            i, j = move[currMove]
            nextRow = currRow + i
            nextCol = currCol + j
            if (nextRow, nextCol) in visited or nextRow < 0 or nextRow == ROWS or nextCol < 0 or nextCol == COLS:
                currMove = nextMove[currMove]
                inxt, jnxt = move[currMove]
                currRow += inxt
                currCol += jnxt
            else:
                currRow += i
                currCol += j

        return res
