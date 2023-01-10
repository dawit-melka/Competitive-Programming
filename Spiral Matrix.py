class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        nextMove = {"right":"down", "down":"left", "left":"up", "up":"right"}
        move = {"right" : [0, 1], "down" : [1, 0], "left" : [0, -1], "up" : [-1, 0]}
        currMove = "right"
        currRow, currCol = 0, 0
        visited = set()
        spiralOrder = []

        while (len(spiralOrder) < ROWS*COLS):
            spiralOrder.append(matrix[currRow][currCol])
            visited.add((currRow, currCol))

            i, j = move[currMove]
            nextRow = currRow + i
            nextCol = currCol + j
            outOfRange = nextRow < 0 or nextRow == ROWS or nextCol < 0 or nextCol == COLS

            if outOfRange or (nextRow, nextCol) in visited:
                currMove = nextMove[currMove]
                inxt, jnxt = move[currMove]
                currRow += inxt
                currCol += jnxt
            else:
                currRow += i
                currCol += j

        return spiralOrder
